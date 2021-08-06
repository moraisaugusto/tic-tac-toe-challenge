# Tic Tac Toe
Anaconda Interview - Test case


## Setup DB
This command will remove the sqlite DB and create a new DB (alembic migration)
```bash
make setup_db
```

## Run backend
This command will start up the Flask app
```bash
make run
```

## Run unittest
```bash
make test
```

### Create a new game

```bash
curl -X POST -H "Content-Type: application/json" \
-d '{"player_one_name":"Augusto", "player_one_mark":"X", "player_two_name":"Flavio", "player_two_mark":"O"}' \
http://localhost:5000/api/games
```

### Retrieve all games

```bash
curl -X GET -H "Content-Type: application/json" http://localhost:5000/api/games
```

### Retrieve One game - ID 5
```bash
curl -X GET -H "Content-Type: application/json" \
http://localhost:5000/api/games/5
```

### Update game - ID 5
```bash
curl -X POST -H "Content-Type: application/json" \
-d '{"player_name":"Augusto", "position": 5}' \
http://localhost:5000/api/games/5
```


## Run scenarios
This will simulate REST requests between 2 players and one of them will win.
```bash
make simulate_win
```

This will simulate REST requests between 2 players and no one will win.
```bash
make simulate_draw
```
This will simulate REST requests between 2 players and a user will try use use 
a board position already used. This will raise an error and return a error message to 
the user.
```bash
make simulate_error
```
