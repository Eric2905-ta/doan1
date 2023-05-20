import psycopg2
from flask import Flask, render_template

app = Flask(__name__)

def get_data():
    # Establish a connection to the PostgreSQL database
    conn = psycopg2.connect(
        host="localhost",
        port="5432",
        database="mydb",
        user="postgres",
        password="eric"
    )

    # Create a cursor object to interact with the database
    cur = conn.cursor()

    # Execute the SQL query to fetch data from the "con" column of the "test" table
    cur.execute("SELECT * from testob where state > '3' ")

    # Fetch all the rows returned by the query
    list_avail = cur.fetchall()

    # Close the cursor and the database connection
    cur.close()
    conn.close()

    return list_avail

def generate_messages(data):
    messages = []
    for element in data:
        message = f" ID {element[0]} in area {element[3]} need support"
        messages.append(message)
    return messages

@app.route('/')
def index():
    # Get data from the database
    data = get_data()

    # Generate the messages
    messages = generate_messages(data)

    # Render the template with the messages
    return render_template('app.html', messages=messages)

if __name__ == '__main__':
    app.run()
