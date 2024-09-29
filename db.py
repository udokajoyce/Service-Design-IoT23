import sqlite3

connection = sqlite3.connect('ApiDatabase.db', check_same_thread=False, timeout=10)
cursor = connection.cursor()

def create_table():
    """Create a table in the database if it doesn't already exist."""
    cursor.execute('''CREATE TABLE IF NOT EXISTS data (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        name TEXT,
                        info TEXT
                    )''')

def get_all_customers():
    """Retrieve all customer records from the database."""
    cursor.execute("SELECT * FROM data")
    return cursor.fetchall()

def get_customer(id):
    """Retrieve a specific customer by ID."""
    cursor.execute("SELECT * FROM data WHERE id=?", [id])
    return cursor.fetchone()

def add_customer(name, info):
    """Insert a new customer record into the database."""
    cursor.execute("INSERT INTO data (name, info) VALUES (?, ?)", [name, info])
    connection.commit()

def close_connection():
    """Close the database connection."""
    connection.close()
