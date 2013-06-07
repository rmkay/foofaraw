import web
from ZODB.FileStorage import FileStorage
from ZODB.DB import DB
import transaction

urls = ('/','index')

storage = FileStorage('Data.fs')
db = DB(storage)
connection = db.open()
root = connection.root()

class Entity(object):
    def __init__(self, string):
        self.string = string

class index:
    def GET(self):
        return "Hello, %s!"(root['1'])

if __name__ == "__main__":

    root['1'] = Entity('world')
    transaction.commit()

    app = web.application(urls,globals())
    app.run()
