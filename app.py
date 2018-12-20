from database import Database
from models.blog import Blog

__author__ = 'Libère'

Database.initialize()

blog = Blog(author="Libere",
            title="Sample Title",
            description="SampleDescription")

blog.new_post()

blog.save_to_mongo()

from_database = Blog.from_mongo(blog.id)

print(blog.get_posts())
