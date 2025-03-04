import sqlite3


def mnthly_aggregate_rating():
    # Create a sql connection
    conn = sqlite3.connect('product_ratings.db')
    # initialise a cursor
    c = conn.cursor()

    # rounding off avg to 2 digits after decimal
    c.execute('''CREATE TABLE IF NOT EXISTS ratingMonthlyAggregates AS
                 SELECT DISTINCT
                 PRODUCT_ID, 
                 strftime('%Y-%m', timestamp) AS YEARMO,
                 ROUND(AVG(RATING),2) AS AVG_RATING 
                 FROM Ratings
                 GROUP BY 1,2; ''')

    print(f"table ratingMonthlyAggregates created successfully.")
    conn.commit()
    conn.close()


if __name__ == '__main__':
    mnthly_aggregate_rating()

