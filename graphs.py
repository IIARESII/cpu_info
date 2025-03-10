import matplotlib.pyplot as plt
import matplotlib.animation as animation
from datetime import datetime
from ani import get_info

# Количество отображаемых точек на графике
MAX_POINTS = 50
# Интервал сохранения графика (в секундах)
SAVE_INTERVAL = 60  # 1 минута

# Списки для хранения данных
cpu_usage_data = []
mem_usage_data = []
time_stamps = []

# Функция обновления графика
def update(frame):
    cpu_usage, mem_usage = get_info().cpu_see()
    current_time = datetime.now().strftime('%H:%M:%S')
    
    # Добавляем новые данные
    cpu_usage_data.append(cpu_usage)
    mem_usage_data.append(mem_usage)
    time_stamps.append(current_time)
    
    # Ограничиваем количество точек
    if len(cpu_usage_data) > MAX_POINTS:
        cpu_usage_data.pop(0)
        mem_usage_data.pop(0)
        time_stamps.pop(0)
    
    # Очищаем график и рисуем заново
    ax.clear()
    ax.plot(cpu_usage_data, label='CPU Usage (%)', color='r')
    ax.plot(mem_usage_data, label='Memory Usage (%)', color='b')
    
    # Настройки графика
    ax.set_ylim(0, 100)
    ax.set_title('Мониторинг загрузки CPU и RAM')
    ax.set_xlabel('Время')
    ax.set_ylabel('Загрузка (%)')
    ax.legend()
    ax.grid()
    
    # Проверяем, нужно ли сохранить график
    if frame % (SAVE_INTERVAL // 2) == 0:  # Учитываем, что update вызывается каждые 2 сек
        save_graph()

# Функция сохранения графика в файл
def save_graph():
    timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    filename = f'cpu_memory_plot_{timestamp}.png'
    plt.savefig(filename)
    print(f'[{timestamp}] График сохранён: {filename}')

# Создание окна с графиком
fig, ax = plt.subplots()
ani = animation.FuncAnimation(fig, update, interval=2000)  # Обновление каждые 2 сек

plt.show()
