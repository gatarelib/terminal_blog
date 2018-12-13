__author__ = 'Libère'

# use the appropriate port
class Database(object):
    URI = 'mongodg://127.0.0.1:****'
    DATABASE = None

    @staticmethod
    def initialize():
        client = pymogo.MongoClient(Database.URI)
        Database.DATABASE = client['fullstack']

    @staticmethod
    def insert(collection, data):
        Database.DATABASE[collection].insert(data)

    @staticmethod
    def find(collection, query):
        Database.DATABASE[collection].find(query)

    @staticmethod
    def find_one(collection, query):
        Database.DATABASE[collection].find_one(query)
