from mysqlconnection import MySQLConnection

class Plant:
    def __init__(self, data):
        self.id = data['id']
        self.plant_name = data['plant_name']
        self.plant_type = data['plant_type']
        self.tools_and_materials = data['tools_and_materials']
        self.plants_component = data['plants_component']
        self.procedure = data['procedure']
        self.user_id = data['user_id']

    @classmethod
    def save(cls, data):
        query = """
        INSERT INTO plant (plant_name, plant_type, tools_and_materials, plants_component, `procedure`, user_id)
        VALUES (%(plant_name)s, %(plant_type)s, %(tools_and_materials)s, %(plants_component)s, %(procedure)s, %(user_id)s);
        """
        return MySQLConnection('plantmanagement').query_db(query, data)

    @classmethod
    def get_all_by_user(cls, data):
        query = "SELECT * FROM plant WHERE user_id = %(user_id)s;"
        results = MySQLConnection('plantmanagement').query_db(query, data)
        return [cls(row) for row in results]

    @classmethod
    def get_by_id(cls, data):
        query = "SELECT * FROM plant WHERE id = %(id)s;"
        result = MySQLConnection('plantmanagement').query_db(query, data)
        return cls(result[0]) if result else None

    @classmethod
    def update(cls, data):
        query = """
        UPDATE plant
        SET plant_name=%(plant_name)s, plant_type=%(plant_type)s,
            tools_and_materials=%(tools_and_materials)s, plants_component=%(plants_component)s,
            `procedure`=%(procedure)s
        WHERE id = %(id)s;
        """
        return MySQLConnection('plantmanagement').query_db(query, data)

    @classmethod
    def delete(cls, data):
        query = "DELETE FROM plant WHERE id = %(id)s;"
        return MySQLConnection('plantmanagement').query_db(query, data)
