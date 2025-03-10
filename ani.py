import psutil
import time
real_password='1234'
names=psutil.users()


while True:
   passcode=input(f'Hi {names[0].name} enter passcode')

   if real_password==passcode:
        break
   else:
        print('wrong try again') 




class get_info:
    def __init__(self) -> None:
        pass 
    def cpu_see(self):
        memory_usage=psutil.virtual_memory().percent
        cpu_usage=psutil.cpu_percent()
        return cpu_usage,memory_usage    
    
    def cpu_see_in_detail(self):
        processes=psutil.process_iter()
        return processes 
        
        
            
    def network_get(self):
        networks=psutil.net_io_counters()
        return networks.bytes_sent/1000000,networks.bytes_recv/1000000
    def awake_time(self):
        boot_time=psutil.boot_time()
        uptime=time.time()-boot_time
        return uptime









