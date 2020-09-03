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
            self.cpu_loader.write_to_cpu_file(self.cpu_loader.get_current_cpu_load())
        
if (__name__ == "__main__"):
    obj = CiscoCpuLoad("172.16.4.2", "admin", "admin123")
    observer = CpuObserver(5, obj)
    observer.start()
    
    while True:
        print(obj.read_from_cpu_file())
        time.sleep(10)