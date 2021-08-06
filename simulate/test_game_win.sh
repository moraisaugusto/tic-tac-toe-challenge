
#!/usr/bin/env sh

game_id=$(curl -X POST -H "Content-Type: application/json" -d '{"player_one_name":"Augusto", "player_one_mark":1, "player_two_name":"Flavio", "player_two_mark":0}' http://localhost:5000/api/games | jq --raw-output '.id')

curl -X POST -H "Content-Type: application/json" \
-d '{"player_name":"Augusto", "position": 1}' \
http://localhost:5000/api/games/$game_id
sleep 0.1


curl -X POST -H "Content-Type: application/json" \
-d '{"player_name":"Flavio", "position": 6}' \
http://localhost:5000/api/games/$game_id
sleep 0.1


curl -X POST -H "Content-Type: application/json" \
-d '{"player_name":"Augusto", "position": 2}' \
http://localhost:5000/api/games/$game_id
sleep 0.1


curl -X POST -H "Content-Type: application/json" \
-d '{"player_name":"Flavio", "position": 4}' \
http://localhost:5000/api/games/$game_id
sleep 0.1

curl -X POST -H "Content-Type: application/json" \
-d '{"player_name":"Augusto", "position": 3}' \
http://localhost:5000/api/games/$game_id
