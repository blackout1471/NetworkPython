from GetRouterTraffic import RouterInfo
import sys
sys.path.append("..")
from GraphMaker import GraphMaker

class BwLoadGraph(GraphMaker):
    def __init__(self, _router_info):
        self.router_info = _router_info
        GraphMaker.__init__(self, "Bandwidth Load Graph", "Time", "Bandwidth %", 5000)
        self.ydata = []
        self.xdata = []
    
    def get_data(self):
        self.ydata.append(self.router_info.current_bw)
        self.xdata.append(len(self.ydata))
            
        return [self.xdata, self.ydata]

if __name__ == "__main__":
    router = RouterInfo('172.16.4.2', 'admin', 'admin123', 'cisco_ios', 'admin1234', 'G0/0', '1000000')
    from BandWidthObserver import BandwidthObserver
    observer = BandwidthObserver(5, router)
    observer.start()

    graph = BwLoadGraph(router)
    graph.Run()
