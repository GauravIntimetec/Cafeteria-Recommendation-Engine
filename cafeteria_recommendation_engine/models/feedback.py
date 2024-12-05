from database import get_db_connection

class Feedback:
    @staticmethod
    def add_feedback(user_id, item_id, comment, rating):
        connection = get_db_connection()
        cursor = connection.cursor()
        cursor.execute("INSERT INTO feedback (user_id, item_id, comment, rating) VALUES (%s, %s, %s, %s)",
                       (user_id, item_id, comment, rating))
        connection.commit()
        cursor.close()
        connection.close()

    @staticmethod
    def get_monthly_feedback():
        connection = get_db_connection()
        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM feedback WHERE MONTH(created_at) = MONTH(CURRENT_DATE)")
        feedbacks = cursor.fetchall()
        cursor.close()
        connection.close()
        return feedbacks

    @staticmethod
    def get_ratings():
        connection = get_db_connection()
        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT item_id, AVG(rating) as average_rating FROM feedback GROUP BY item_id")
        ratings = cursor.fetchall()
        cursor.close()
        connection.close()
        return ratings
