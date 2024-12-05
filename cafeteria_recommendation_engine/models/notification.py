from cafeteria_recommendation_engine.models.database import get_db_connection

class Notification:
    @staticmethod
    def create(message, recipient_role):
        connection = get_db_connection()
        cursor = connection.cursor()
        cursor.execute("INSERT INTO notifications (message, recipient_role) VALUES (%s, %s)",
                       (message, recipient_role))
        connection.commit()
        cursor.close()
        connection.close()

    @staticmethod
    def get_notifications(recipient_role):
        connection = get_db_connection()
        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM notifications WHERE recipient_role = %s", (recipient_role,))
        notifications = cursor.fetchall()
        cursor.close()
        connection.close()
        return notifications
