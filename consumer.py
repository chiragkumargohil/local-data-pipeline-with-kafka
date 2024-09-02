import json
from kafka import KafkaConsumer
from database_setup import insert_data

# Initialize Kafka Consumer
consumer = KafkaConsumer(
    'user_activity',
    bootstrap_servers='localhost:9092',
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    group_id='user_activity_group'
)

if __name__ == "__main__":
    print("Consumer is running...")
    for message in consumer:
        try:
            # Decode the message and load it as a JSON object
            data = json.loads(message.value.decode('utf-8'))
            
            # Insert data into the database
            insert_data(data['user_id'], data['username'], data['action'], data['timestamp'])
            print(f"Inserted: {data}")

        except json.JSONDecodeError as e:
            print(f"Error decoding JSON: {e}")
        except Exception as e:
            print(f"Unexpected error: {e}")