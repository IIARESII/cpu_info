
import time
import tkinter as tk
from threading import Thread
from ani import get_info

class SystemMonitorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("System Monitor")
        self.root.geometry("600x400")
        
        self.text_area = tk.Text(root, height=15, width=70)
        self.text_area.pack()
        
        self.btn_cpu = tk.Button(root, text="Show CPU Info", command=self.show_cpu_info)
        self.btn_cpu.pack()
        
        self.btn_mem = tk.Button(root, text="Show Memory Info", command=self.show_mem_info)
        self.btn_mem.pack()
        
        self.btn_net = tk.Button(root, text="Show Internet Info", command=self.show_internet_info)
        self.btn_net.pack()
        
        self.btn_cpu_detail = tk.Button(root, text="CPU Detail Usage", command=self.cpu_detail_usage)
        self.btn_cpu_detail.pack()
        
        self.btn_time = tk.Button(root, text="System Uptime", command=self.time_see)
        self.btn_time.pack()
        
        self.btn_stop = tk.Button(root, text="Stop Monitoring", command=self.stop_monitoring)
        self.btn_stop.pack()
        
        self.running = False
    
    def log_message(self, message):
        self.text_area.insert(tk.END, message + "\n")
        self.text_area.see(tk.END)
    
    def run_task(self, func):
        self.running = True
        thread = Thread(target=func, daemon=True)
        thread.start()
    
    def show_cpu_info(self):
        def task():
            while self.running:
                self.log_message(f'CPU usage: {get_info().cpu_see()[0]} %')
                time.sleep(1)
        self.run_task(task)
    
    def show_mem_info(self):
        def task():
            while self.running:
                self.log_message(f'Memory usage: {get_info().cpu_see()[1]} %')
                time.sleep(1)
        self.run_task(task)
    
    def show_internet_info(self):
        def task():
            while self.running:
                self.log_message(f'Mb/s out: {get_info().network_get()[0]:.2f} | Mb/s in: {get_info().network_get()[1]:.2f}')
                time.sleep(1)
        self.run_task(task)
    
    def cpu_detail_usage(self):
        def task():
            while self.running:
                for process in get_info().cpu_see_in_detail():
                    self.log_message(f"PID: {process.pid}, Name: {process.name()}, CPU: {process.cpu_percent()}%, Mem: {process.memory_percent():.2f}%")
                time.sleep(1)
        self.run_task(task)
    
    def time_see(self):
        self.log_message(f'System has been running for {round(get_info().awake_time()/3600, 2)} hours')
    
    def stop_monitoring(self):
        self.running = False

if __name__ == "__main__":
    root = tk.Tk()
    app = SystemMonitorApp(root)
    root.protocol("WM_DELETE_WINDOW", app.stop_monitoring)  # Остановить мониторинг при закрытии
    root.mainloop()
