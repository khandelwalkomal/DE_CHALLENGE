import sqlite3


def top3_products():
    conn = sqlite3.connect('product_ratings.db')
    c = conn.cursor()

    # using dense_rank() as multiple products can have same avg_rating for a month
    # taking all product if they qualify for the same rank
    result = c.execute('''
        SELECT * FROM 
        (
            SELECT DISTINCT
            YEARMO,
            PRODUCT_ID,
            DENSE_RANK() OVER(PARTITION BY YEARMO ORDER BY AVG_RATING DESC) AS RANK
            FROM ratingMonthlyAggregates 
        )A
        WHERE RANK <=3
        ORDER BY YEARMO, RANK;
    ''').fetchall()
    conn.close()
    return result


if __name__ == '__main__':
    top_products = top3_products()
    for product in top_products:
        print(product)

