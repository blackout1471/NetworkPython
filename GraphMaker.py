from matplotlib import pyplot
import matplotlib.animation as animation
from CiscoCpuLoad import CiscoCpuLoad

class GraphMaker:
    def __init__(self, title, xlabel, ylabel, updateRate):
        self.title = title
        self.xlabel = xlabel
        self.ylabel = ylabel
        self.updaterate = updateRate

        self.fig = pyplot.figure()
        self.ax1 = self.fig.add_subplot(1, 1, 1)
     
    
    def animate(self, i):
        data = self.get_data()
        self.ax1.clear()
        self.ax1.plot(data[0], data[1])
        
    def get_data(self):
        return None
        
    def Run(self):
        ani = animation.FuncAnimation(self.fig, self.animate, interval=self.updaterate)
        self.ax1.set_title(self.title)
        self.ax1.set_xlabel(self.xlabel)
        self.ax1.set_ylabel(self.ylabel)
        pyplot.show()
    
    