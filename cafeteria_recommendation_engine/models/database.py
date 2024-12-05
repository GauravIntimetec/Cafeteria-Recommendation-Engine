import mysql.connector
from mysql.connector import errorcode

def get_db_connection():
    try:
        connection = mysql.connector.connect(
            user='admin',
            password='Football@11',
            host='localhost',
            database='recomendation_db'
        )
        return connection
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)

def create_database():
    connection = get_db_connection()
    cursor = connection.cursor()
    try:
        cursor.execute(
            "CREATE DATABASE IF NOT EXISTS cafeteria_db DEFAULT CHARACTER SET 'utf8'"
        )
    except mysql.connector.Error as err:
        print(f"Failed creating database: {err}")
        exit(1)
    cursor.close()
    connection.close()

def create_tables():
    connection = get_db_connection()
    cursor = connection.cursor()

    TABLES = {}
    TABLES['users'] = (
        "CREATE TABLE IF NOT EXISTS `users` ("
        "  `user_id` varchar(20) NOT NULL,"
        "  `name` varchar(50) NOT NULL,"
        "  `role` varchar(20) NOT NULL,"
        "  PRIMARY KEY (`user_id`)"
        ") ENGINE=InnoDB")

    TABLES['menu_items'] = (
        "CREATE TABLE IF NOT EXISTS `menu_items` ("
        "  `item_id` int NOT NULL AUTO_INCREMENT,"
        "  `name` varchar(100) NOT NULL,"
        "  `price` decimal(5,2) NOT NULL,"
        "  `availability` boolean NOT NULL,"
        "  PRIMARY KEY (`item_id`)"
        ") ENGINE=InnoDB")

    TABLES['notifications'] = (
        "CREATE TABLE IF NOT EXISTS `notifications` ("
        "  `notification_id` int NOT NULL AUTO_INCREMENT,"
        "  `message` varchar(255) NOT NULL,"
        "  `recipient_role` varchar(20) NOT NULL,"
        "  PRIMARY KEY (`notification_id`)"
        ") ENGINE=InnoDB")

    TABLES['votes'] = (
        "CREATE TABLE IF NOT EXISTS `votes` ("
        "  `vote_id` int NOT NULL AUTO_INCREMENT,"
        "  `user_id` varchar(20) NOT NULL,"
        "  `item_id` int NOT NULL,"
        "  PRIMARY KEY (`vote_id`)"
        ") ENGINE=InnoDB")

    TABLES['feedback'] = (
        "CREATE TABLE IF NOT EXISTS `feedback` ("
        "  `feedback_id` int NOT NULL AUTO_INCREMENT,"
        "  `user_id` varchar(20) NOT NULL,"
        "  `item_id` int NOT NULL,"
        "  `comment` text,"
        "  `rating` int,"
        "  PRIMARY KEY (`feedback_id`)"
        ") ENGINE=InnoDB")

    for table_name in TABLES:
        table_description = TABLES[table_name]
        try:
            cursor.execute(table_description)
        except mysql.connector.Error as err:
            print(f"Failed creating table {table_name}: {err}")
            exit(1)

    cursor.close()
    connection.close()


# con = get_db_connection()
# print(con)