import re

def get_numbers_from_string(data):
    return re.findall(r'\d+', data)
    
def get_line_from_string(number, data):
    return data.partition('\n')[number]