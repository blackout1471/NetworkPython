import sys
import os
from netmiko import ConnectHandler

sys.path.append("..")
from Filehandler import FileHandler
import Formathandler as fh


class CiscoCpuLoad:
    def __init__(self, ip, username, password):
        self.connect_handler = ConnectHandler(device_type="cisco_ios", ip=ip, username=username, password=password)
        filePath = os.path.join(os.path.dirname(__file__), "cpuLoad.txt")
        self.file_handler = FileHandler(filePath)
        
        
    def get_five_minutes_cpu_load(self):
        data = self.__get_cpu_table_load()
        data = fh.get_line_from_string(0, data)
        data = fh.get_numbers_from_string(data)
        return data[-1]
        
    def get_current_cpu_load(self):
        data = self.__get_cpu_table_load()
        data = fh.get_line_from_string(0, data)
        data = fh.get_numbers_from_string(data)
        if (data[0] == None):
            data = [None]
        
        return data[0];
        
    def write_to_cpu_file(self, data):
        self.file_handler.append_to_file(fh.format_cpu_data_tostring(data))
        
    def read_from_cpu_file(self):
        dataList = []
        data = self.file_handler.read_from_file()
        data = fh.get_lines_from_string(data)
        
        for line in data:
            if line != "":
                dataList.append(fh.format_cpu_data_toobject(line))
        
        return dataList
    
    def __get_cpu_table_load(self):
        return self.connect_handler.send_command("show process cpu")
        
        
if (__name__ == "__main__"):
    d = CiscoCpuLoad("172.16.4.2", "admin", "admin123")
    print(d.get_five_minutes_cpu_load())