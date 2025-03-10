        
# def monitoring(cpu_usage,mem_usage,bars=50):
#     cpu_percent=(cpu_usage/100.0)
#     cpu_bar='#' * int(cpu_percent * bars) + '-' * (bars-int(cpu_percent)*bars)
#
#     mem_percent=(mem_usage/100.0)
#     mem_bar='#' * int(mem_percent * bars) + '-' * (bars-int(mem_percent)*bars)
#


import turtle  
import tkinter as tk  

def draw_circle():  
    t.clear()  
    t.circle(50)  

root = tk.Tk()  
root.title("Простое GUI с Turtle")  

button = tk.Button(root, text="Нарисовать круг", command=draw_circle)  
button.pack()  

canvas = turtle.ScrolledCanvas(root)  
canvas.pack()  

t = turtle.RawTurtle(canvas)  

root.mainloop()
