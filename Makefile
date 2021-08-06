.PHONY: setup_db run test simulate_win simulate_draw simulate_error

default: run

setup_db:
	rm db.sqlite && alembic upgrade head

run:
	./start.sh

test:
	PYTHONPATH=. pytest -vvv

simulate_win:
	./simulate/test_game_win.sh

simulate_draw:
	./simulate/test_game_draw.sh

simulate_error:
	./simulate/test_game_error.sh

