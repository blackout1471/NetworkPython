import re
from datetime import datetime

def get_lines_from_string(data):
    return data.split('\n')

def get_numbers_from_string(data):
    return re.findall(r'\d+', data)
    
def get_line_from_string(number, data):
    return data.partition('\n')[number]
    
def format_cpu_data_tostring(data):
    return data + ";" + datetime.now().strftime("%H:%M:%S")
    
def format_cpu_data_toobject(data):
    dataObj = {
    "load":None,
    "hours":None,
    "minutes":None,
    "seconds":None,
    }
    
    splitData = data.split(";")
    dataObj["load"] = splitData[0]
    
    splitDate = splitData[1].split(":")
    
    dataObj["hours"] = splitDate[0]
    dataObj["minutes"] = splitDate[1]
    dataObj["seconds"] = splitDate[2]
    
    return dataObj
    