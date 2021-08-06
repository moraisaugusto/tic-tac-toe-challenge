from flask import Flask, request, jsonify

from src.helper import is_json_request
from src.modules.tic_tac_toe.actions import (
    new_game,
    retrieve_games,
    update_game)


app = Flask(__name__)


@app.route("/api/games", methods=["GET", "POST"])
@is_json_request
def games():
    if request.method == "POST":
        game_id = new_game(request.json)
        return jsonify({
            "status": "new game created",
            "id": game_id
        }), 200

    list_games = retrieve_games()
    return jsonify({
        "status": "games listed",
        "message": list_games
    }), 200


@app.route("/api/games/<game_id>", methods=["GET", "POST"])
@is_json_request
def game(game_id: int = None):
    if request.method == "POST":
        board, winner = update_game(request.json, game_id)

        return jsonify({
            "status": "game updated",
            "message": board,
            "winner": winner
        }), 200

    list_games = retrieve_games(game_id)
    return jsonify({
        "status": "game retrieved",
        "message": list_games
    }), 200


@app.errorhandler(Exception)
def unhandled_exception(e):
    print(e)
    http_code = 500 if not hasattr(e, "code") else e.code
    error_msg = "{}".format(str(e))

    return jsonify({
        "status": False,
        "message": error_msg
    }), http_code


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
