import numpy
from matplotlib import pyplot
from CiscoCpuLoad import CiscoCpuLoad
import time

class CpuLoadGraph:
    def __init__(self, ciscoCpuLoad):
        self.cpuLoader = ciscoCpuLoad
        pyplot.title("Cpu Load Graph")
        pyplot.xlabel("Time : HH/MM/SS")
        pyplot.ylabel("Cpu Load %")
        pyplot.ion()
        
        data = self.__get_cpu_data()
        
        fig = pyplot.figure()
        ax = fig.add_subplot(111)
        line1, = ax.plot(data[1], data[0])
        
        while True:
            
        
        pyplot.figure()
        
    def plot_data(self):
        data = self.cpuLoader.read_from_cpu_file()
        load_arr = []
        time_arr = []
        
        for item in data:
            load = int(item["load"])
            time = int(item["hours"])*10000 + int(item["minutes"])*100 + int(item["seconds"])
            load_arr.append(load)
            time_arr.append(time)
        pyplot.plot(time_arr, load_arr)
        
    def __get_cpu_data(self):
        data = self.cpuLoader.read_from_cpu_file()
        load_arr = []
        time_arr = []
        
        for item in data:
            load = int(item["load"])
            time = int(item["hours"])*10000 + int(item["minutes"])*100 + int(item["seconds"])
            load_arr.append(load)
            time_arr.append(time)
         
        return [load_arr, time_arr]

if __name__ == "__main__":
    obj = CiscoCpuLoad("172.16.4.2", "admin", "admin123")
    graph = CpuLoadGraph(obj)
    import time
    time.sleep(10)
    print("done")