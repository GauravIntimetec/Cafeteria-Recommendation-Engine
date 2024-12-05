from cafeteria_recommendation_engine.models.database import get_db_connection

def create_db_and_tables():
    create_database()
    create_tables()

def init_db():
    connection = get_db_connection()
    cursor = connection.cursor()
    return cursor
    # users = [
    #     ('admin1', 'Admin One', 'admin'),
    #     ('chef1', 'Chef One', 'chef'),
    #     ('emp1', 'Employee One', 'employee'),
    # ]
    # for user in users:
    #     cursor.execute("INSERT INTO users (user_id, name, role) VALUES (%s, %s, %s)", user)
    # connection.commit()
    # cursor.close()
    # connection.close()

print(init_db())
