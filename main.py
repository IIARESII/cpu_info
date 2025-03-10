import psutil
import time
import os 
import matplotlib.pyplot as plt
        
# def monitoring(cpu_usage,mem_usage,bars=50):
#     cpu_percent=(cpu_usage/100.0)
#     cpu_bar='#' * int(cpu_percent * bars) + '-' * (bars-int(cpu_percent)*bars)
#
#     mem_percent=(mem_usage/100.0)
#     mem_bar='#' * int(mem_percent * bars) + '-' * (bars-int(mem_percent)*bars)
#


while True:
    mem_usge_all=psutil.virtual_memory().percent
    cpu_all_usage=psutil.cpu_percent()
    processes = psutil.process_iter()
    network2=psutil.net_io_counters()
    network=psutil.net_connections()
    for process in processes:
        print(f"Process ID: {process.pid}, Name: {process.name()},Cpu:{process.cpu_percent()}, Mem_usage:{process.memory_percent():.2f}%")
    print('Cpu all usage',cpu_all_usage)
    print('mem usage',mem_usge_all)
    print(network2.bytes_sent/1000000,network2.bytes_recv/1000000)

    
    time.sleep(1) 
    

