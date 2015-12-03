from Client import Connection
import json

cn = Connection.Connection()
coba = "loginanjing"

cn.send(json.dumps(coba))
print(cn.recv())

coba = "createroomanjing_goreng"
cn.send(json.dumps(coba))
print(cn.recv())


