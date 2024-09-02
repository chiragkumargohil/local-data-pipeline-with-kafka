# Local Data Pipeline with Kafka and SQLite

## Project Overview

This project implements a local data pipeline that generates synthetic user activity data, streams it using Apache Kafka, processes it with a consumer, and stores it in a SQLite database. The project also includes data visualization features to analyze user actions.

## Technologies Used

- **Python**: Programming language for data generation, processing, and visualization.
- **Docker**: Containerization platform for running Kafka and Zookeeper.
- **Kafka**: Distributed streaming platform for handling real-time data streams.
- **Zookeeper**: Coordination service for distributed systems.
- **SQLite**: Lightweight database for storing user activity data.
- **Faker**: Library for generating synthetic data.
- **Pandas**: Data manipulation and analysis library.
- **Matplotlib**: Library for creating visualizations.

## Getting Started

### Installation

1. **Clone the repository**:

   ```
   git clone https://github.com/chiragkumargohil/local-data-pipeline-with-kafka.git
   cd local-data-pipeline-with-kafka
   ```

2. **Install dependencies**:

   ```
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

   OR

   ```
   pip install kafka-python-ng faker pandas matplotlib sqlite3
   ```

3. **Start Zookeeper and Kafka**:

   ```
   docker compose up -d
   ```

4. **Create the Kafka topic**:

   ```
   docker exec -it [kafka_container_id] kafka-topics.sh --create --topic user_activity --bootstrap-server localhost:9092 --replication-factor 1 --partitions 1
   ```

5. **Create SQLite database**:
   ```
   python3 database_setup.py
   ```
6. **Run the producer and consumer**:
   ```
   python3 producer.py
   python3 consumer.py
   ```
7. **Visualize the data**:
   ```
   python3 visualize.py
   ```

## Data Generation

The data generation process uses the `Faker` library to create synthetic user activity data. The data includes the following fields:

- `id`: Unique identifier.
- `user_id`: Unique identifier for the user.
- `name`: Name of the user.
- `action`: Type of user action (e.g., click, page_view).
- `timestamp`: Time when the action occurred.

The data is generated in real-time and streamed to Kafka using the `producer.py` script.

## Data Processing

The data processing step involves consuming the data from Kafka, transforming it into a `pandas` DataFrame, and storing it in a SQLite database. The `consumer.py` script reads the data from Kafka, processes it, and inserts it into the SQLite database.

## Data Visualization

The data visualization step involves analyzing the user activity data stored in the SQLite database. The `visualize.py` script reads the data from the database, creates visualizations using `matplotlib`, and displays them in the terminal.
