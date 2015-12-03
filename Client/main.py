from Client import Connection
import json

cn = Connection.Connection()
coba = "login2"

cn.send(json.dumps(coba))


