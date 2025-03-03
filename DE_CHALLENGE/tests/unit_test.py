import unittest
import sqlite3
from DE_CHALLENGE.src.de_challenge.top3_products import top3_products


class ProjectTest(unittest.TestCase):

    def test_generate_data(self):
        # Ensure that data is populated
        conn = sqlite3.connect('product_ratings.db')
        c = conn.cursor()
        c.execute('SELECT COUNT(*) FROM Ratings')
        count = c.fetchone()[0]
        conn.close()
        self.assertGreater(count, 0, "Database should have some ratings data")

    def test_compute_aggregates(self):
        # Ensure that aggregates are computed
        conn = sqlite3.connect('product_ratings.db')
        c = conn.cursor()
        c.execute('SELECT COUNT(*) FROM ratingMonthlyAggregates')
        count = c.fetchone()[0]
        self.assertGreater(count, 0, "Aggregates table should have some data")

        conn.close()

    def test_compute_aggregates_values(self):
        # compute_monthly_aggregates()

        # Ensure that aggregates are computed
        conn = sqlite3.connect('product_ratings.db')
        c = conn.cursor()
        c.execute('SELECT COUNT(*) FROM ratingMonthlyAggregates where average_rating <0.0 or average_rating >5.0')
        count = c.fetchone()[0]
        self.assertEqual(0, count, "Table should always have ratings between 0.0 to 5.0")

        conn.close()

    def test_find_top_products(self):
        top_products_out = top3_products()

        # Ensure correct top products are found
        self.assertIsInstance(top_products_out, list, "Top products should be a list")
        self.assertGreater(len(top_products_out), 0, "There should be some top products")


if __name__ == '__main__':
    unittest.main()
