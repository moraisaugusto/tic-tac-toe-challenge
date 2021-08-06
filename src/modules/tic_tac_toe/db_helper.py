import pickle

from sqlalchemy import exc

from db_models import Game
from src.lib.db_helper import DatabaseBase


class Database(DatabaseBase):

    @staticmethod
    def create_game(user_request):
        """Create a new game"""
        try:
            session = DatabaseBase.db_session()
            board = pickle.dumps([[" "," "," "], [" "," "," "], [" "," "," "]])
            game = Game(
                player_one_name=user_request["player_one_name"],
                player_one_mark=user_request["player_one_mark"],
                player_two_name=user_request["player_two_name"],
                player_two_mark=user_request["player_two_mark"],
                board=board,
                last_player=user_request["player_two_name"],
                done=False)
            session.add(game)
            session.commit()
            game_id = game.id
            session.close()
        except exc.SQLAlchemyError as e:
            print("Error persisting a new game", e)
        except Exception as e:
            print("Error persisting a new game", e)

        return game_id

    @staticmethod
    def update_board(board: dict, game_id: int, player_name: str):
        """get the mark of the user

        Args:
            board (dict): current game to be updated in DB
            game_id (int): game id
            player_name (str): player name
        Results:
            True if success, otherwise False
        """
        try:
            session = DatabaseBase.db_session()
            session.query(Game).filter(Game.id == game_id).update({
                Game.board: pickle.dumps(board),
                Game.last_player: player_name
            })
            session.commit()
            session.close()
            return True
        except exc.SQLAlchemyError as e:
            print("Error updating the game", e)
        except Exception as e:
            print("Error updating the game", e)

        return False

    @staticmethod
    def set_game_over(game_id, winner):
        """set game over"""
        session = DatabaseBase.db_session()
        session.query(Game).filter(Game.id == game_id).update({
            Game.winner: winner,
            Game.done: True
        })
        session.commit()
        session.close()
