import json
from glob import glob

from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer

authorizer = DummyAuthorizer()
userfiles = glob('users/*.json')
for userfile in userfiles:
    with open(userfile, "r", encoding="utf-8")as file:
        user = json.load(file)
    authorizer.add_user(user['username'], user['password'], user['rootpath'], perm='elradfmwMT')

handler = FTPHandler
handler.authorizer = authorizer

server = FTPServer(("0.0.0.0", 21), handler)

if __name__ == '__main__':
    server.serve_forever()
