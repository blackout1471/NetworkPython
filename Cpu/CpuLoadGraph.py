import sys
import time
from CiscoCpuLoad import CiscoCpuLoad

sys.path.append("..")
from GraphMaker import GraphMaker


class CpuLoadGraph(GraphMaker):
    def __init__(self, ciscoCpuLoader):
        self.data_loader = ciscoCpuLoader
        GraphMaker.__init__(self, "Cpu Load Graph", "Time", "Cpu %", 5000)
    
    def get_data(self):
        data = self.data_loader.read_from_cpu_file()
        xdata = []
        ydata = []
        
        i = 0
        for item in data:
            ydata.append(int(item["load"]))
            xdata.append(i)
            i+=1
            
        return [xdata, ydata]

if __name__ == "__main__":
    obj = CiscoCpuLoad("172.16.4.2", "admin", "admin123")
    from CpuObserver import CpuObserver
    observer = CpuObserver(5, obj)
    observer.start()
    
    graph = CpuLoadGraph(obj)
    graph.Run()