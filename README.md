Real-Time Weather Monitoring with Kafka & PostgreSQL  

Project Overview  
This project fetches real-time weather data from the OpenWeatherMap API and streams it using Apache Kafka. The data is then consumed and stored in PostgreSQL, making it ready for further analysis or visualization in BI tools like Apache Superset.  

Tech Stack  
- Data Streaming: Apache Kafka  
- Database: PostgreSQL  
- Programming Language: Python  
- Dependencies: kafka-python, requests, psycopg2  

Project Structure  
Real-Time-Weather-Monitoring  
 - kafka_producer.py      Fetches weather data and sends to Kafka  
 - kafka_consumer.py      Reads Kafka stream and inserts into PostgreSQL  
 - requirements.txt       Python dependencies  
 - README.md              Project documentation  

Setup Instructions  

1. Install Dependencies  
Ensure you have Python 3.8+ installed. Then, install the required libraries:  

pip install -r requirements.txt  

2. Start Kafka  

# Start Zookeeper  
zookeeper-server-start.sh config/zookeeper.properties  

# Start Kafka Broker  
kafka-server-start.sh config/server.properties  

3. Run PostgreSQL and Create Database  
Run the following SQL command to create the required table:  

CREATE TABLE weather_data (  
    id SERIAL PRIMARY KEY,  
    city VARCHAR(50),  
    temperature FLOAT,  
    humidity INT,  
    pressure INT,  
    weather VARCHAR(100),  
    wind_speed FLOAT,  
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP  
);  

4. Run Producer and Consumer  

# Start producer to fetch weather data and send to Kafka  
python kafka_producer.py  

# Start consumer to read from Kafka and store in PostgreSQL  
python kafka_consumer.py  

Future Improvements  
- Store historical weather trends for better analysis  
- Implement real-time alerts for extreme weather conditions  
- Optimize Kafka streaming for better performance  

Learning Outcomes  
- Using Kafka for real-time data streaming  
- Integrating PostgreSQL for structured data storage  
- Handling live API data and automating workflows  

License  
This project is licensed under the MIT License.  

Contact  
Email: gannavaramsridhar9515@gmail.com 
LinkedIn: https://www.linkedin.com/in/gannavaram-sridhar/ 
