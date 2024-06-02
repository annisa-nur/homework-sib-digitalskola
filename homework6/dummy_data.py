import csv
import datetime
import random

# Buat data dummy
header = ['order_id', 'order_date', 'user_id', 'payment_name', 'shipper_name', 'order_price', 'order_discount', 'voucher_name', 'voucher_price', 'order_total', 'rating_status']
data = []

for i in range(1, 1001):
    order_date = datetime.datetime(2023, random.randint(1, 12), random.randint(1, 28)).strftime('%Y-%m-%d')
    data.append([i, order_date, random.randint(1, 100), 'Credit Card', 'FedEx', random.uniform(10.0, 500.0), random.uniform(1.0, 50.0), 'DISCOUNT10', random.uniform(0.0, 10.0), random.uniform(10.0, 500.0), 'Completed'])

# Tulis data dummy ke CSV
with open('orders.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(header)
    writer.writerows(data)

print("Dummy data created and saved to orders.csv")
