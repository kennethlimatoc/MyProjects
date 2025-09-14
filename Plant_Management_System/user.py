from mysqlconnection import MySQLConnection

class User:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.username = data['username']
        self.password_hash = data['password_hash']

    @classmethod
    def save(cls, data):
        query = """
        INSERT INTO userlist (first_name, last_name, email, username, password_hash)
        VALUES (%(first_name)s, %(last_name)s, %(email)s, %(username)s, %(password_hash)s);
        """
        return MySQLConnection('plantmanagement').query_db(query, data)

    @classmethod
    def get_by_username(cls, username):
        query = "SELECT * FROM userlist WHERE username = %(username)s;"
        data = {"username": username}
        results = MySQLConnection('plantmanagement').query_db(query, data)
        if not results:
            return False
        return cls(results[0])
    
    @classmethod
    def get_by_id(cls, data):
        query = "SELECT * FROM userlist WHERE id = %(id)s;"
        results = MySQLConnection('plantmanagement').query_db(query, data)
        if results:
            return cls(results[0])
        return None
    
    @classmethod
    def update(cls, data):
        query = """
        UPDATE userlist 
        SET first_name = %(first_name)s,
            last_name = %(last_name)s,
            email = %(email)s,
            username = %(username)s,
            password_hash = %(password_hash)s
        WHERE id = %(id)s;
        """
        return MySQLConnection('plantmanagement').query_db(query, data)