# DE_CHALLENGE
DE CHALLENGE to calculate Monthly average ratings and top products

## Steps to execute 

navigate to the Source package where all the Python modules are.

Step 1 - Clone the repository in your local machine and install the dependencies using poetry 

```poetry install```

Step 2 - Execute create_data.py in poetry to create a Database and Ratings table with random data

```poetry run python create_data.py```

Step 3 - Execute mnthly_aggregates.py using poetry that will generate monthly average ratings for products and store it in a table RatingsMonthlyAggregates.

```poetry run python mnthly_aggregates.py```

Step 4 - Execute top3_products.py to list three top-rated products for every month of 2024 in RatingsMonthlyAggregates table created in the previous step.

```poetry run python top3_products.py```

Step 5 - Execute below command to run the unit tests.

```poetry run python -m unittest unit_tests.py```
