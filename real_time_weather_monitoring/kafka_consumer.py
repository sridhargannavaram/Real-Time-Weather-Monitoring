from kafka import KafkaConsumer
import psycopg2
import json

# Kafka Consumer setup
consumer = KafkaConsumer(
    'weather_topic',  # Kafka topic
    bootstrap_servers=['localhost:9092'],  # Adjust to your Kafka server
    group_id='weather_group',
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))  # Deserialize JSON data
)

# PostgreSQL connection
conn = psycopg2.connect(
    dbname="weather_db",  # Replace with your database name
    user="sreedhar",     # Replace with your PostgreSQL username
    password="Sree@8688",  # Replace with your PostgreSQL password
    host="localhost",     # Replace with your PostgreSQL host
    port="5432"           # Replace with your PostgreSQL port (default is 5432)
)
cursor = conn.cursor()

# Function to insert weather data into PostgreSQL
def insert_weather_data(data):
    try:
        cursor.execute("""
            INSERT INTO weather_data (city, timestamp, temperature, humidity, wind_speed)
            VALUES (%s, %s, %s, %s, %s)
        """, (data['city'], data['timestamp'], data['temperature'], data['humidity'], data['wind_speed']))
        conn.commit()
        print(f"Data inserted into PostgreSQL for city: {data['city']}")
    except Exception as e:
        print(f"Error inserting data into PostgreSQL: {e}")
        conn.rollback()

# Consumer loop to consume data from Kafka and insert into PostgreSQL
print("Starting Kafka Consumer...")
try:
    for message in consumer:
        weather_data = message.value  # Get the data from Kafka
        print("Received weather data:", weather_data)
        insert_weather_data(weather_data)  # Insert data into PostgreSQL
except KeyboardInterrupt:
    print("Stopping Kafka Consumer...")
finally:
    # Close database connection
    cursor.close()
    conn.close()
    print("Database connection closed.")

