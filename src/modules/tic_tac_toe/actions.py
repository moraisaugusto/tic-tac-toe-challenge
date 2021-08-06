import pickle
from werkzeug.exceptions import NotFound, BadRequest

from db_models import Game
from src.lib.db_helper import DatabaseBase
from src.modules.tic_tac_toe.helper import Helper
from src.modules.tic_tac_toe.db_helper import Database
from src.modules.tic_tac_toe import tic_tac_toe


def update_game(user_request: dict, game_id: int):
    """update a game

    Args:
        user_request (dict): basic data to update game
        game_id (int): Id of the game
    Results:
        board game
    """
    if not game_id:
        raise NotFound("Game ID not defined")

    game_id = int(game_id)
    player_name = user_request["player_name"]
    position = user_request["position"]

    current_game = retrieve_games(game_id)[0]
    board = current_game["board"]
    player = Helper.get_user_mark(current_game, user_request)

    if player_name == current_game["last_player"]:
        raise BadRequest(f"{player_name}, It's not your turn.")

    if current_game["done"]:
        raise BadRequest("Game already finished. Create a new one")

    # check if players exist in the game
    if not Helper.players_exit(user_request, current_game):
        raise BadRequest("Player not found in the current game.")

    has_machine = Helper.is_playing_alone(current_game)

    # update board game
    board = tic_tac_toe.update_game(board, position, player, has_machine)

    # check winner
    winner = Helper.get_winner(board, player_name)
    if winner or winner == "Draw game!":
        Database.set_game_over(game_id, player_name)

    if has_machine:
        machine = 0 if int(player) else 1
        player_name = "MACHINE"
        machine_position = tic_tac_toe.machine_move(board)
        tic_tac_toe.update_game(board, machine_position, machine)

        # check winner
        winner = Helper.get_winner(board, player_name)
        if winner or winner == "Draw game!":
            Database.set_game_over(game_id, player_name)

    # update board game in db
    Database.update_board(board, game_id, player_name)

    return board, winner


def new_game(user_request: dict):
    """create new game

    Args:
        user_request (dict): basic data to create a new game

    Returns:
        id of the new game
    """
    if user_request["player_one_name"] == user_request["player_two_name"]:
        raise ValueError("You can not use equal names.")

    game_id = Database.create_game(user_request)

    return game_id


def retrieve_games(game_id: int = None):
    """retrieve one or all games from the DB

    Args:
        user_request (None | int): if none returns all games otherwise one id

    Returns:
        return a list of games in DB
    """
    session = DatabaseBase.db_session()
    if game_id:
        rows = [session.query(Game).filter_by(id=game_id).one_or_none()]
    else:
        rows = session.query(Game).all()

    if not rows[0]:
        raise NotFound("Id not found")

    # TODO: please improve me
    entries = []
    for row in rows:
        entry = row.__dict__
        entry["board"] = pickle.loads(entry["board"])
        del entry["_sa_instance_state"]
        entries.append(entry)

    return entries
