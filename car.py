from mysqlconnection import MySQLConnection

class model:
    def __init__(self, data):
        self.id = data['id']
        self.Make = data['Make']
        self.Model = data['Model']
        self.Year = data['Year']
        self.Description = data['Description']

    @classmethod
    def add_cars(cls, data):
        query = "INSERT INTO model (Make, Model, Year, Description) VALUES (%(Make)s, %(Model)s, %(Year)s,%(Description)s);"
        return MySQLConnection('cars').query_db(query, data)

    @classmethod
    def display_cars(cls):
        query = "SELECT * FROM model;"
        results = MySQLConnection('cars').query_db(query)
        cars = []
        for result in results:
            cars.append(cls(result)) 
        return cars
    
    #for delete to nakakalito
    @classmethod
    def delete_info(cls, data):
        query = "DELETE FROM model WHERE id = %(id)s;"
        return MySQLConnection('cars').query_db(query, data)
    
    
   #for update to
   
    @classmethod
    def update_info(cls, data):
        query = "UPDATE model SET Make=%(Make)s, Model=%(Model)s, Year=%(Year)s, Description=%(Description)s WHERE id = %(id)s;"
        return MySQLConnection('cars').query_db(query, data)
    
    @classmethod
    def retrieve_info(cls, data):
        query = "SELECT * FROM model WHERE id = %(id)s;"
        results = MySQLConnection('cars').query_db(query, data)
        cars = []
        for result in results:
            cars.append(cls(result)) 
        return cars

   
    