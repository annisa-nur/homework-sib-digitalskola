from confluent_kafka import avro
from confluent_kafka.avro import AvroConsumer

# Configure the AvroConsumer
avro_consumer = AvroConsumer({
    'bootstrap.servers': 'localhost:9092',
    'group.id': 'bitcoin_price_group',
    'schema.registry.url': 'http://localhost:8081',
    'auto.offset.reset': 'earliest'
})

# Subscribe to the Kafka topic
avro_consumer.subscribe(['bitcoin_price_topic'])

# Consume messages from the Kafka topic
print("Consuming messages from the topic:")
while True:
    try:
        msg = avro_consumer.poll(10)
        if msg is None:
            continue

        record = msg.value()
        print(record)

    except KeyboardInterrupt:
        break
    except Exception as e:
        print(f"Error: {e}")
        continue

avro_consumer.close()
