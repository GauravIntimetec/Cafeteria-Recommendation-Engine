from cafeteria_recommendation_engine.models.database import get_db_connection

class MenuItem:
    @staticmethod
    def add_item(name, price, availability):
        connection = get_db_connection()
        cursor = connection.cursor()
        cursor.execute("INSERT INTO menu_items (name, price, availability) VALUES (%s, %s, %s)",
                       (name, price, availability))
        connection.commit()
        cursor.close()
        connection.close()

    @staticmethod
    def remove_item(item_id):
        connection = get_db_connection()
        cursor = connection.cursor()
        cursor.execute("DELETE FROM menu_items WHERE item_id = %s", (item_id,))
        connection.commit()
        cursor.close()
        connection.close()

    @staticmethod
    def update_item(item_id, name, price, availability):
        connection = get_db_connection()
        cursor = connection.cursor()
        cursor.execute("UPDATE menu_items SET name = %s, price = %s, availability = %s WHERE item_id = %s",
                       (name, price, availability, item_id))
        connection.commit()
        cursor.close()
        connection.close()

    @staticmethod
    def change_price(item_id, new_price):
        connection = get_db_connection()
        cursor = connection.cursor()
        cursor.execute("UPDATE menu_items SET price = %s WHERE item_id = %s", (new_price, item_id))
        connection.commit()
        cursor.close()
        connection.close()

    @staticmethod
    def update_availability(item_id, availability):
        connection = get_db_connection()
        cursor = connection.cursor()
        cursor.execute("UPDATE menu_items SET availability = %s WHERE item_id = %s", (availability, item_id))
        connection.commit()
        cursor.close()
        connection.close()

    @staticmethod
    def get_todays_menu():
        connection = get_db_connection()
        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM menu_items WHERE availability = 1")
        menu_items = cursor.fetchall()
        cursor.close()
        connection.close()
        return menu_items
