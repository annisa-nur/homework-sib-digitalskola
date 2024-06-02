from hadoop_connection import upload_to_hdfs

# Upload orders.csv to Hadoop
upload_to_hdfs('orders.csv', '/user/orders.csv')
