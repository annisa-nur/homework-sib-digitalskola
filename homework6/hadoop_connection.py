import json
import requests
from hdfs import InsecureClient                                                                                                                                                                             # type: ignore

# Load Hadoop connection details from json
with open('hadoop.json') as f:
    hadoop_config = json.load(f)['hadoop']

client = InsecureClient(f"http://{hadoop_config['host']}:{hadoop_config['port']}", user=hadoop_config['username'])

# Example function to upload file to HDFS
def upload_to_hdfs(local_path, hdfs_path):
    client.upload(hdfs_path, local_path)
    print(f"Uploaded {local_path} to {hdfs_path}")

# Usage
upload_to_hdfs('orders.csv', '/user/orders.csv')
