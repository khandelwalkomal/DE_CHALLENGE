import sqlite3

def drop_table():
    # Create a sql connection
    conn = sqlite3.connect('product_ratings.db')
    # initialise a cursor
    c = conn.cursor()
    c.execute('''DROP TABLE IF EXISTS ratingMonthlyAggregates; ''')
    print(f"table ratingMonthlyAggregates dropped successfully.")
    conn.commit()
    conn.close()


if __name__ == '__main__':
    drop_table()

