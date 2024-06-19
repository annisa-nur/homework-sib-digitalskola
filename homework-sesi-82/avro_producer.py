import pandas as pd
from confluent_kafka import avro
from confluent_kafka.avro import AvroProducer

# Load the dataset
file_path = 'bitcoin_price_Training.xlsx'
bitcoin_data = pd.read_excel(file_path)

# Define the Avro schema
schema_str = """
{
  "type": "record",
  "name": "BitcoinPrice",
  "fields": [
    {"name": "Date", "type": "string"},
    {"name": "Open", "type": "float"},
    {"name": "High", "type": "float"},
    {"name": "Low", "type": "float"},
    {"name": "Close", "type": "float"},
    {"name": "Volume", "type": "float"},
    {"name": "MarketCap", "type": "float"}
  ]
}
"""

schema = avro.loads(schema_str)

# Configure the AvroProducer
avro_producer = AvroProducer({
    'bootstrap.servers': 'localhost:9092',
    'schema.registry.url': 'http://localhost:8081'
}, default_value_schema=schema)

# Produce messages to the Kafka topic
topic = 'bitcoin_price_topic'

for index, row in bitcoin_data.iterrows():
    record = {
        "Date": str(row['Date']),
        "Open": row['Open'],
        "High": row['High'],
        "Low": row['Low'],
        "Close": row['Close'],
        "Volume": row['Volume'],
        "MarketCap": row['MarketCap']
    }
    avro_producer.produce(topic=topic, value=record)
    avro_producer.flush()

print("Produced all messages")
