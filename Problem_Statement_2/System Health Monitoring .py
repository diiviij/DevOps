import logging
from datetime import datetime


logging.basicConfig(filename='systemhealth.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')


CPU_THRESHOLD = 80  
MEMORY_THRESHOLD = 80  
DISK_THRESHOLD = 80  
def check_cpu():
    cpu_usage = psutil.cpu_percent(interval=1)
    if cpu_usage > CPU_THRESHOLD:
        alert_message = f"High CPU usage detected: {cpu_usage}%"
        alert(alert_message)

def check_memory():
    memory_info = psutil.virtual_memory()
    memory_usage = memory_info.percent
    if memory_usage > MEMORY_THRESHOLD:
        alert_message = f"High Memory usage detected: {memory_usage}%"
        alert(alert_message)

def check_disk():
    disk_info = psutil.disk_usage('/')
    disk_usage = disk_info.percent
    if disk_usage > DISK_THRESHOLD:
        alert_message = f"High Disk usage detected: {disk_usage}%"
        alert(alert_message)

def check_processes():
    process_count = len(psutil.pids())
    logging.info(f"Running processes: {process_count}")

def alert(message):
    print(message)
    logging.warning(message)

def main():
    logging.info("System Health Monitoring Script Started")
    while True:
        check_cpu()
        check_memory()
        check_disk()
        check_processes()
        
        time.sleep(60)

if __name__ == "__main__":
    main()
