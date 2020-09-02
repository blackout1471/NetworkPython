import threading
from CiscoCpuLoad import CiscoCpuLoad
import time

class CpuObserver(threading.Thread):
    def __init__(self, seconds, ciscoCpuLoader):
        self.sleep_time = seconds
        self.cpu_loader = ciscoCpuLoader
        threading.Thread.__init__(self)
        self.daemon = True
    
    def run(self):
        while True:
            time.sleep(self.sleep_time)
            self.cpu_loader.write_to_cpu_file(self.cpu_loader.get_five_minutes_cpu_load())
        
if (__name__ == "__main__"):
    observer = CpuObserver(5, CiscoCpuLoad("172.16.4.2", "admin", "admin123"))
    observer.start()
    
    while True:
        time.sleep(2000)