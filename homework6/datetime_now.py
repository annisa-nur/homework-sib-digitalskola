from datetime import datetime

def get_current_datetime():
    return datetime.now().strftime('%Y-%m-%d %H:%M:%S')

print(f"Current datetime: {get_current_datetime()}")
