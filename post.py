import uuid
from models.database import Database
import datetime

__author__ = 'Libère'


class Post(object):

    def __init__(self, title, content, author, date=datetime.datetime.utcnow(), id=None):
        self.blog_id = blog_id
        self.title  = title
        self.content = content
        self.author = author
        self.created_date = date
        self.id = uuid.uuid4().hex if id is None else id


    def save_to_mongo(self):
        Database.insert(collection='post',
                        data=self.json())

    def json(self):
        return {
            'id' : self.id,
            'blog_id' : self.blog_id,
            'author' : self.author,
            'content' : self.content,
            'title' : self.title,
            'created_date' : self.created_date
        }

    @staticmethod
    def from_mongo(id):
        return Database.find(collection='posts', query={'id':id})

    @staticmethod
    def from_blog(id):
        return [post for post in Database.find(collection='posts', query={'blog_id':id})]
