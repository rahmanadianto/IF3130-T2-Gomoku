from Client import Connection
import json

cn = Connection.Connection()
contoh = list()
contoh.append(2)
contoh.append(4)
cek = json.dumps(contoh)

cn.send(cek)


