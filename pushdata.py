import random
from datetime import date, datetime

import psycopg2
from psycopg2 import Error

# Connect to the PostgreSQL database
try:
    connection = psycopg2.connect(
        host="localhost",
        port="5432",
        database="mydb",
        user="postgres",
        password="eric"
    )

    cursor = connection.cursor()

    # Generate and insert 50 rows of data
    for _ in range(50):
        id_val = random.randint(1, 100)
        source_val = 1
        frame_val = random.randint(1, 100)
        roid_val = random.choice(['A', 'B', 'C', 'D'])
        state_val = random.randint(1, 4)
        time_val = datetime.now().date()

        insert_query = f"INSERT INTO testob (id, source, frame, roid, state, time) VALUES ({id_val}, {source_val}, {frame_val}, '{roid_val}', {state_val}, '{time_val}')"
        cursor.execute(insert_query)

    connection.commit()
    print("Data inserted successfully!")

except (Exception, Error) as error:
    print("Error while connecting to PostgreSQL or inserting data:", error)

finally:
    if connection:
        cursor.close()
        connection.close()
        print("PostgreSQL connection closed.")
