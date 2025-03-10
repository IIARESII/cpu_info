import time
from ani import get_info
print('Hi this program can show data about system')
command_list=['show_cpu_info','show_mem_info','show_internet_info','cpu_detail_usage','time_see']

while True:
    print('Ypu can use only this command',command_list)
    vvod=input('you can type here>>>  ')
    if vvod==command_list[0]:
        try:
            while True:
                print(f'cpu usage  {get_info().cpu_see()[0]} %')
                time.sleep(1)
        except KeyboardInterrupt:
            print()
    elif vvod==command_list[1]:
        try:
            while True:
                print(f'mem usage  {get_info().cpu_see()[1]} %')
                time.sleep(1)
        except KeyboardInterrupt:
            print()
    elif vvod==command_list[2]:
        try:
            while True:
                print(f'mgbits out {get_info().network_get()[0]:.2f}||||| mgbits in {get_info().network_get()[1]:.2f}')
                
                time.sleep(1)
        except KeyboardInterrupt:
            print()
    elif vvod==command_list[3]:
        try:
            while True:
                for process in get_info().cpu_see_in_detail():
                    print(f"Process ID: {process.pid}, Name: {process.name()},Cpu:{process.cpu_percent()}, Mem_usage:{process.memory_percent():.2f}%")
                time.sleep(1)
        except KeyboardInterrupt:
            print()
    elif vvod==command_list[4]:
        print('System are working about',round(get_info().awake_time()/3600,2),'hours')
