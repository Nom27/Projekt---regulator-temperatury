import serial
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np

# Port szeregowy
SERIAL_PORT = 'COM5'  # Zmień na odpowiedni port
BAUD_RATE = 9600

# Inicjalizacja portu
ser = serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=1)

# Bufory danych
time_data = []
setpoint_data = []
temperature_data = []
pwm_data = []
time_elapsed = 0

def update_plot(frame):
    global time_elapsed

    # Odczyt danych z portu
    line = ser.readline().decode('utf-8').strip()
    if line:
        try:
            parts = line.split(',')
            setpoint = float(parts[0].split(':')[1].strip())
            temperature = float(parts[1].split(':')[1].strip())
            pwm = float(parts[2].split(':')[1].strip())

            # Aktualizacja buforów
            time_data.append(time_elapsed)
            setpoint_data.append(setpoint)
            temperature_data.append(temperature)
            pwm_data.append(pwm)
            time_elapsed += 1

            # Aktualizacja wykresu
            ax1.clear()
            ax2.clear()

            ax1.plot(time_data, setpoint_data, label='Setpoint (°C)', color='blue')
            ax1.plot(time_data, temperature_data, label='Temperature (°C)', color='red')
            ax1.set_title('Temperature Control')
            ax1.set_ylabel('Temperature (°C)')
            ax1.legend()
            ax1.grid()
            ax1.set_xlim(left=0, right=max(time_data))  # Oś X zaczyna się od 0 i rozciąga do maksymalnej wartości czasu

            ax2.plot(time_data, pwm_data, label='PWM (%)', color='green')
            ax2.set_title('PWM Duty Cycle')
            ax2.set_ylabel('PWM (%)')
            ax2.legend()
            ax2.grid()
            ax2.set_xlim(left=0, right=max(time_data))  # Oś X zaczyna się od 0 i rozciąga do maksymalnej wartości czasu

        except Exception as e:
            print(f"Error parsing line: {line} -> {e}")

# Tworzenie wykresów
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8))
ani = FuncAnimation(fig, update_plot, interval=1000)

plt.show()
