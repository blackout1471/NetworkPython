import paramiko
import netmiko
import sys
sys.path.append("..")
import Formathandler as fh

class InterfaceInfo:
    def __init__(self, _interface_name, _max_bandwidth):
        self.interface_name = _interface_name
        self.max_bandwidth = _max_bandwidth

class RouterInfo:
    def __init__(self, _ip, _username, _password, _device_type, _secret, _interface_name, _max_bandwidth):
        self.ip = _ip
        self.username = _username
        self.password = _password
        self.device_type = _device_type
        self.secret = _secret
        self.interface = InterfaceInfo(_interface_name, _max_bandwidth)
        self.current_bw = float(0)
        
    def values(self):
        router_values = {
            'ip': self.ip,
            'username': self.username,
            'password': self.password,
            'device_type': self.device_type,
            'secret': self.secret,
        }
        return router_values
    
    def GetCurrentBandwidth(self):
        r1 = netmiko.ConnectHandler(**self.values())
        r1.enable()
        raw_str = r1.send_command('sh int ' + self.interface.interface_name)
        r1.disconnect()
        string_arr = fh.get_lines_from_string(raw_str)
        input_rate = fh.get_numbers_from_string(string_arr[15])[1]
        output_rate = fh.get_numbers_from_string(string_arr[16])[1]
        final_bw = int(output_rate) + int(input_rate)
        return final_bw

    def CalculateBandwidthPercent(self):
        curr_bw = self.GetCurrentBandwidth()
        if curr_bw == 0:
            self.current_bw = 0
        else:
            bw_percent = curr_bw / int(self.interface.max_bandwidth)
            bw_percent = bw_percent * 100
            self.current_bw = float(bw_percent)

if (__name__ == "__main__"):
    router = RouterInfo('172.16.4.2', 'admin', 'admin123', 'cisco_ios', 'admin1234', 'G0/0', '1000000')
    router.CalculateBandwidthPercent()
    print(router.current_bw)



