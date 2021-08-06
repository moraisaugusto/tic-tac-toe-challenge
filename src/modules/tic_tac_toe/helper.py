from werkzeug.exceptions import BadRequest

from src.modules.tic_tac_toe import tic_tac_toe


class Helper():

    #staticmethod
    def is_playing_alone(current_game):
        """If second player has the name MACHINE, the plays alone"""
        if "MACHINE" in current_game.values():
            return True
        return False

    @staticmethod
    def get_user_mark(current_game: dict, user_request: dict):
        """get the mark of the user

        Args:
            current_game (dict): current game from DB
            user_request (dict): data from user request
        Results:
            player_mark
        """
        player_number = None
        for title, value in current_game.items():
            if value == user_request["player_name"]:
                player_number = 1 if "_one_" in title else 2
                break

        if not player_number:
            raise BadRequest("User not found in this game")

        if player_number == 1:
            player_mark = current_game["player_one_mark"]
        else:
            player_mark = current_game["player_two_mark"]

        return player_mark

    @staticmethod
    def get_winner(board: dict, player_name: str):
        """get the game winner

        Args:
            board (dict): current board game
            player_name (str): player name
        Returns:
            returns winner game
        """
        winner = None
        if tic_tac_toe.check_win(board):
            winner = f"Player {player_name} won!"
            return winner

        if not tic_tac_toe.free_slots(board):
            if not winner:
                winner = "Draw game!"
                return winner

        return winner

    @staticmethod
    def players_exit(user_request, current_game):
        """check if players exist in the game

        Args:
            user_request (dict): json user request
            current_game (dict): game dataset from db
        Returns:
            True if exists otherwise, False
        """
        if user_request["player_name"] in current_game.values():
            return True
        return False
