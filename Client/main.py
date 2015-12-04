from Client import Connection
import json
from Gameplay import Board

board = Board.Board()
cn = Connection.Connection()
coba = '{"type":"login", "name" : "anjing"}'

cn.send(coba)
terima = json.loads(cn.recv().decode("UTF-8"))
if terima['state'] == "success":
    print(terima['type'] + " berhasillllll!!!!!")
    print(terima['user_id'])
else:
    print("gagaaaallllll :(")

coba = '{"type":"join_room", "room_id" : "1"}'
cn.send(coba)
terima = json.loads(cn.recv().decode("UTF-8"))
#print(terima)
if terima['state'] == "success":
    print(terima['type'] + " berhasillllll!!!!!")
    print(terima['room_id'])
else:
    print(terima['type'] + " gagaaaallllll :(")
print("board room ini: \n")
print(board.board)
cn.send('{"type":"start","user_id":"1"}')
terima = json.loads(cn.recv().decode("UTF-8"))
gerak = '{"type":"move","user_id":"1","x":"0","y":"1"}'
board.startGame()
cn.send(gerak)
terima = json.loads(cn.recv().decode("UTF-8"))
board.placeonBoard(int(terima['x']),int(terima['y']),terima['pion'])
print(board.board)


