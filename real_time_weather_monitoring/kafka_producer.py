from kafka import KafkaProducer
import requests
import json
import time

# OpenWeatherMap API key
API_KEY = "bcc2576860c85915337e77396181e112"

# List of cities for which you want to fetch weather data
CITIES = ["Delhi", "Mumbai", "Bangalore", "Chennai", "Hyderabad", "Kolkata", "Pune", "Jaipur", "Kochi", "Chandigarh"]

# Kafka Producer setup
producer = KafkaProducer(
    bootstrap_servers=['localhost:9092'],  # Adjust to your Kafka server
    value_serializer=lambda v: json.dumps(v).encode('utf-8')  # Serialize data as JSON
)

# Kafka Topic
TOPIC = 'weather_topic'

# Function to fetch weather data for a specific city
def fetch_weather_data(city):
    # Use the `units=metric` parameter to get temperature in Celsius
    API_URL = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    try:
        response = requests.get(API_URL)
        data = response.json()
        if response.status_code == 200:
            weather_data = {
                "city": city,
                "timestamp": time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime()),  # Get current timestamp
                "temperature": data['main']['temp'],  # Temperature in Celsius
                "humidity": data['main']['humidity'],  # Humidity in percentage
                "wind_speed": data['wind']['speed']  # Wind speed in m/s
            }
            return weather_data
        else:
            print(f"Failed to fetch data for {city}: {data.get('message', 'Unknown error')}")
            return None
    except Exception as e:
        print(f"Error fetching data for {city}: {e}")
        return None

# Producer loop to send data to Kafka every minute for all cities
print("Starting Kafka Producer...")
while True:
    for city in CITIES:
        weather_data = fetch_weather_data(city)
        if weather_data:
            producer.send(TOPIC, value=weather_data)
            print(f"Data sent to Kafka for {city}:", weather_data)
    time.sleep(60)  # Fetch data every 60 seconds

