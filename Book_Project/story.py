from mysqlconnection import MySQLConnection

class stories:
    def __init__(self, data):
        self.id = data['id']
        self.title = data['title']
        self.author = data['author']
        self.year = data['year']
        self.plot = data['plot']

    @classmethod
    def add_story(cls, data):
        query = "INSERT INTO story (title, author, year, plot) VALUES (%(title)s, %(author)s, %(year)s, %(plot)s);"
        return MySQLConnection('story').query_db(query, data)