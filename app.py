from models.database import Database
from models.post import Post

__author__ = 'Libère'

Database.initialize()

post = Post(blog_id="123",
            title="Another great post",
            author="Libère")

post.save_to_mongo()
