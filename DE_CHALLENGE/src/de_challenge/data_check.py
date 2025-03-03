import sqlite3


def verify_data():
    conn = sqlite3.connect('product_ratings.db')
    c = conn.cursor()
    result = c.execute('''
        select * from ratingMonthlyAggregates limit 10;
    ''').fetchall()
    conn.close()
    return result


if __name__ == '__main__':
    count = verify_data()
    print(count)

