import tkinter as tk
from Factors import Factors
from Predicter import Predicter


def calculate_delay():
    left_turns = int(entry_left_turns.get())
    right_turns = int(entry_right_turns.get())
    traffic_level = float(entry_traffic.get())
    distance = float(entry_distance.get())
    weather = weather_var.get()
    day = day_var.get()
    time = int(entry_time.get())

    factors = Factors(left_turns, right_turns, traffic_level, distance, weather, day, time)

    predicter = Predicter()
    delay = predicter.predict(factors)

    result_label.config(text=f"Задержка: {delay} минут")

root = tk.Tk()
root.title("Прогноз задержки")

tk.Label(root, text="Количество поворотов налево:").pack()
entry_left_turns = tk.Entry(root)
entry_left_turns.pack()

tk.Label(root, text="Количество поворотов направо:").pack()
entry_right_turns = tk.Entry(root)
entry_right_turns.pack()

tk.Label(root, text="Уровень трафика (от 0 до 10):").pack()
entry_traffic = tk.Entry(root)
entry_traffic.pack()

tk.Label(root, text="Расстояние (в км):").pack()
entry_distance = tk.Entry(root)
entry_distance.pack()

tk.Label(root, text="Погода:").pack()
weather_var = tk.StringVar(value="Солнечно")
tk.OptionMenu(root, weather_var, "Солнечно", "Облачно", "Дождь", "Снег").pack()

tk.Label(root, text="День недели:").pack()
day_var = tk.StringVar(value="Weekday")
tk.OptionMenu(root, day_var, "Weekday", "Weekend").pack()

tk.Label(root, text="Время (в 24-часовом формате):").pack()
entry_time = tk.Entry(root)
entry_time.pack()

tk.Button(root, text="Рассчитать задержку", command=calculate_delay).pack()

result_label = tk.Label(root, text="", justify="left")
result_label.pack()

root.mainloop()