import sqlite3


def verify_data(tbl_nm):
    conn = sqlite3.connect('product_ratings.db')
    c = conn.cursor()
    result = c.execute(f'''
        select * from {tbl_nm} limit 10;
    ''').fetchall()
    conn.close()
    return result


if __name__ == '__main__':
    rating_data = verify_data("ratings")
    print(f"ratings data: {rating_data}")

    aggregates_data = verify_data("ratingMonthlyAggregates")
    print(f"aggregates data: {aggregates_data}")



