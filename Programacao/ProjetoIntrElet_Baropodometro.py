import serial
import matplotlib.pyplot as plt
import numpy as np

# Configurações do gráfico
fig, ax = plt.subplots(figsize=(90.5/25.4, 260/25.4))  # converter mm para polegadas
fig.canvas.manager.set_window_title('Baropodometria')
ax.set_xlim(0, 90.5)
ax.set_ylim(0, 260)
ax.set_title('Baropodometria')

# Coordenadas dos sensores e diâmetro
sensor_coords = [
    (44, 27),
    (39, 84),
    (62.5, 109),
    (32, 160),
    (68, 193),
    (22, 221)
]
sensor_diameter = 18.5

# Desenhar os sensores no gráfico
sensor_circles = []
for (x, y) in sensor_coords:
    circle = plt.Circle((x, y), sensor_diameter / 2, color='blue', fill=False)
    sensor_circles.append(circle)
    ax.add_patch(circle)

# Configurações da conexão serial
serial_port = 'COM7'
baud_rate = 115200

ser = serial.Serial(serial_port, baud_rate)

def update_plot(forces):
    ax.cla()
    ax.set_xlim(0, 90.5)
    ax.set_ylim(0, 260)
    ax.set_title('Baropodometria')
    
    for circle in sensor_circles:
        ax.add_patch(circle)
    
    for i, force in enumerate(forces):
        x, y = sensor_coords[i]
        normalized_force = force / 80.0
        color_intensity = plt.cm.viridis(normalized_force)
        sensor_fill_circle = plt.Circle((x, y), sensor_diameter / 2, color=color_intensity, fill=True)
        ax.add_patch(sensor_fill_circle)
    
    fig.canvas.draw()
    fig.canvas.flush_events()

plt.ion()
plt.show()

try:
    while True:
        if ser.in_waiting > 0:
            line = ser.readline().decode('utf-8').strip()
            try:
                force_values = list(map(float, line.split(',')))
                if len(force_values) == 6:
                    print(f"Leitura das forças: {force_values}")
                    update_plot(force_values)
                else:
                    print(f"Leitura incorreta: {line}")
            except ValueError:
                print(f"Erro ao converter a linha em floats: {line}")
                continue
except KeyboardInterrupt:
    print("Interrompido pelo usuário")
finally:
    ser.close()
    plt.ioff()
    plt.show()
