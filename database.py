__author__ = 'Libère'


class Database(object):
    URI = 'mongodg://127.0.0.1:27017'
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
        return Database.DATABASE[collection].find(query)

    @staticmethod
    def find_one(collection, query):
        return Database.DATABASE[collection].find_one(query)
