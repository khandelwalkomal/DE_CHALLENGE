import sqlite3
from datetime import datetime, timedelta
import random


def database_create():
    # Create a sql connection
    conn = sqlite3.connect('product_ratings.db')

    # initialise a cursor
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS Ratings(timestamp DATE,user_id INT,product_id INT,rating INT)''')
    print(f"table created successfully.")
    conn.commit()
    conn.close()


def populate_data():
    # Create a sql connection
    conn = sqlite3.connect('product_ratings.db')

    # Initialise a cursor
    c = conn.cursor()
    start_date = datetime(2024, 1, 1)
    end_date = datetime(2024, 12, 31)

    diff = end_date - start_date

    for i in range(100000):
        # generating random data within the given limits
        timestamp = start_date + timedelta(days=random.randint(0, diff.days))
        user_id = random.randint(1, 1000)
        product_id = random.randint(1, 1000)
        rating = random.randint(1, 5)

        c.execute(
            f'''INSERT INTO Ratings (timestamp, user_id, product_id, rating) 
            VALUES ('{timestamp}', {user_id}, {product_id}, {rating})
            ''')

    conn.commit()
    conn.close()


if __name__ == '__main__':
    database_create()
    populate_data()
