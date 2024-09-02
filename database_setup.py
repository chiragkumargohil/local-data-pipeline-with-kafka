import sqlite3

"""Create a SQLite database and user_activity table."""
connection = sqlite3.connect('local.db')
cursor = connection.cursor()

def create_database():
    # Create a table for user activity data
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS user_activity (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id TEXT NOT NULL,
            username TEXT NOT NULL,
            action TEXT NOT NULL,
            timestamp TEXT NOT NULL
        )
    ''')

    connection.commit()
    connection.close()
    print("Database and table created successfully.")

# Insert data into the database
def insert_data(user_id, username, action, timestamp):
    """Insert user activity data into the database."""
    cursor.execute('''
        INSERT INTO user_activity (user_id, username, action, timestamp)
        VALUES (?, ?, ?, ?)
    ''', (user_id, username, action, timestamp))
    connection.commit()

if __name__ == "__main__":
    create_database()