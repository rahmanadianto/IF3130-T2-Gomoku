from Client import Connection
import json

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

coba = '{"type":"leave_room", "user_id" : "1"}'
cn.send(coba)
terima = json.loads(cn.recv().decode("UTF-8"))
if terima['state'] == "success":
    print(terima['type'] + "berhasillllll!!!!!")
    print(terima['room_id'])
else:
    print(terima['type'] + " gagaaaallllll :(")

coba = '{"type":"logout", "user_id" : "1"}'
cn.send(coba)


