import mysql.connector
from opal_common.fetcher.fetch_provider import BaseFetchProvider
from opal_common.fetcher.events import FetcherConfig, FetchEvent
from opal_common.logger import logger
import getpass

MYSQL_CONFIG = {
    'host': 'localhost',
    'database': '',
    'user': '',
    'password': ''
}


def connect_to_mysql():
    try:
        conn = mysql.connector.connect(**MYSQL_CONFIG)
        print("Connected to MySQL!")
        return conn
    except mysql.connector.Error as err:
        print(f"Error connecting to MySQL: {err}")
        return None


def fetch_data_from_mysql(conn, query):
    if not conn:
        print("Not connected to MySQL.")
        return None
    try:
        cursor = conn.cursor()
        cursor.execute(query)
        rows = cursor.fetchall()
        for row in rows:
            print(row)
        cursor.close()
        return rows
    except mysql.connector.Error as err:
        print(f"Error executing query: {err}")
        return None


def authenticate_user(username, password):
    """
    Authentication function using Opal-Common.
    """
    valid_users = {
        "Aman": "hello@123",
        "Bob": "tritikam@67",
    }

    if username in valid_users and valid_users[username] == password:
        return True
    else:
        return False


def authorize_user_with_opal_common(username, password):

    authenticated = authenticate_user(username, password)

    if authenticated:
        print(f"User '{username}' authenticated successfully.")
        return True
    else:
        print(f"Authentication failed for user '{username}'.")
        return False


def main():
    conn = connect_to_mysql()
    if conn:
        username = input("Enter username: ")
        password = getpass.getpass("Enter password: ")
        if authorize_user_with_opal_common(username, password):
            fetch_data_from_mysql(conn, query="SELECT * FROM <table-name>")
        else:
            print("Authorization failed.")
    if conn:
        conn.close()


if __name__ == "__main__":
    main()
