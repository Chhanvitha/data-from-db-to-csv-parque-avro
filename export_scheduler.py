import schedule
import time
from data_exporter import fetch_and_export_data  
# Run every day at 2:00 AM
schedule.every().day.at("02:00").do(fetch_and_export_data)

print("📅 Scheduler started. Waiting to run at 02:00 AM daily...")

while True:
    schedule.run_pending()
    time.sleep(60)
