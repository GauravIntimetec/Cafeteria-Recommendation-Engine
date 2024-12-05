from database import get_db_connection
from admin import Admin
# from .chef import Chef
# from .employee import Employee


class User:

    def __init__(self, name):
        # self.user_id = user_id
        self.name = name
        # self.role = role

    @classmethod
    def login(cls, name):
        connection = get_db_connection()
        print(f"Connection: {connection}")

        cursor = connection.cursor(dictionary=True)
        print(f"Cursor: {cursor}")

        # Debug: print the SQL query to be executed
        query = "SELECT * FROM Users WHERE name = %s"
        print(f"Executing query: {query} with parameter: {name}")

        cursor.execute(query, (name,))
        user_data = cursor.fetchone()
        print(f"User data: {user_data}")


        connection.close()

        if user_data:
            if user_data['role'] == 'Admin':
                print("Login Successful ")
                return Admin(user_data['user_id'], user_data['name'], user_data['role'])
            elif user_data['role'] == 'chef':
                
                return Chef(user_data['user_id'], user_data['name'], user_data['role'])
            elif user_data['role'] == 'employee':
                
                return Employee(user_data['user_id'], user_data['name'], user_data['role'])
        return None


a = User("Amit Sharma")

res = a.login(a.name)
print(res)
