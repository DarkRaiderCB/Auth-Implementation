# MySQL Data Fetcher

This project is a simple MySQL data fetcher that connects to a MySQL database, authenticates a user, and fetches data from a specified table. It uses the `mysql.connector` library to interact with the MySQL database and the `opal_common` library for user authentication.

## Requirements

- Python 3.x
- `mysql-connector-python` library
- `opal_common` library

## Installation

1. Install the required libraries:
    ```bash
    pip install mysql-connector-python opal-common
    ```

2. Ensure you have MySQL installed and running on your machine or accessible from your machine.

## Configuration

Update the `MYSQL_CONFIG` dictionary in the code with your MySQL database details:
```python
MYSQL_CONFIG = {
    'host': 'localhost',
    'database': 'your_database_name',
    'user': 'your_username',
    'password': 'your_password'
}
```


## Usage

1. Connect to MySQL: The script attempts to connect to the MySQL database using the provided configuration.

2. User Authentication: The user is prompted to enter a username and password. Authentication is performed using the opal_common library.

3. Fetch Data: If the user is authenticated successfully, data is fetched from the job_data table in the MySQL database.
