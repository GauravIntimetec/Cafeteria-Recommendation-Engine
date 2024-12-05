from cafeteria_recommendation_engine.models.database import get_db_connection

class Vote:
    @staticmethod
    def cast_vote(user_id, item_id):
        connection = get_db_connection()
        cursor = connection.cursor()
        cursor.execute("INSERT INTO votes (user_id, item_id) VALUES (%s, %s)", (user_id, item_id))
        connection.commit()
        cursor.close()
        connection.close()

    @staticmethod
    def get_today_votes():
        connection = get_db_connection()
        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT item_id, COUNT(*) as count FROM votes GROUP BY item_id")
        votes = cursor.fetchall()
        cursor.close()
        connection.close()
        return votes
