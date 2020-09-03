import threading
from GetRouterTraffic import RouterInfo
import time

class BandwidthObserver(threading.Thread):
    def __init__(self, _seconds, _router_info):
        self.sleep_time = _seconds
        self.router_info = _router_info
        threading.Thread.__init__(self)
        self.daemon = True

    def run(self):
        while True:
            time.sleep(self.sleep_time)
            self.router_info.CalculateBandwidthPercent()
            
if (__name__ == "__main__"):
    r1 = RouterInfo('172.16.4.2', 'admin', 'admin123', 'cisco_ios', 'admin1234', 'G0/0', '1000000')
    observer = BandwidthObserver(5, r1)
    observer.start()

    while True:
        #print(observer.router_info.current_bw)
        time.sleep(10)
    
