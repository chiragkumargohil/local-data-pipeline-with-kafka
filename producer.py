import time
import json
from kafka import KafkaProducer
from kafka.errors import KafkaError
from faker import Faker

# Initialize Faker and Kafka Producer
fake = Faker()
producer = KafkaProducer(bootstrap_servers='localhost:9092')

def produce_data():
    """Generate synthetic user activity data."""
    while True:
        try:
        # Create a dictionary with synthetic data
            data = {
                'user_id': fake.uuid4(),
                'username': fake.user_name(),
                'action': fake.random_element(elements=('login', 'logout', 'click', 'form_submit', 'page_view')),
                'timestamp': fake.date_time_this_month().isoformat()
            }
            
            # Send data to Kafka topic
            producer.send('user_activity', json.dumps(data).encode('utf-8'))
            print(f"Sent: {data}")
            
            # Wait for a while before generating the next record
            time.sleep(1)
        except KafkaError as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    produce_data()