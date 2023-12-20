import os
from ksp_computing import *
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import ticker


if not os.path.isdir("графики_ksp"):  # папка для хранения графиков
    os.mkdir("графики_ksp")

# Вытаскиваем расчеты
time = np.array(time_array)
height = np.array(height_array)
mass = np.array(mass_of_rocket_array)
velocity = np.array(velocity_scalar_array)
acceleration = np.array(acceleration_array)
angle = np.array(angel_array)
pressure = np.array(pressure_array)
ro = np.array(ro_array)
# drag_force = np.array(drag_force_array)
position = np.array(position_array)
force_of_gravity = np.array(force_of_gravity_array)
thrust_of_force = np.array(force_of_thrust_array)

# Построение графиков
fig, ax = plt.subplots(figsize=(11, 8))  # график скорости от времени
plt.plot(time, velocity, color='darkgreen', linewidth=4)
ax.set_title("Зависимость скорости от времени", fontsize=20)
ax.set_xlabel('Время, с', fontsize=14)
ax.set_ylabel('Скорость, м/с', fontsize=14)
ax.tick_params(axis='both', which='major', labelsize=14)
formatter = ticker.ScalarFormatter()
formatter.set_scientific(False)
ax.yaxis.set_major_formatter(formatter)
ax.xaxis.set_major_formatter(formatter)
fig.tight_layout()
plt.savefig("графики_ksp/график_скорости_от_времени.png")

fig, ax = plt.subplots(figsize=(11, 8))  # график высоты от времени
plt.plot(time, height, color='deepskyblue', linewidth=4)
ax.set_title("Зависимость высоты от времени", fontsize=20)
ax.set_xlabel('Время, с', fontsize=14)
ax.set_ylabel('Высота, м', fontsize=14)
ax.tick_params(axis='both', which='major', labelsize=14)
formatter = ticker.ScalarFormatter()
formatter.set_scientific(False)
ax.yaxis.set_major_formatter(formatter)
ax.xaxis.set_major_formatter(formatter)
fig.tight_layout()
plt.savefig("графики_ksp/график_высоты_от_времени.png")

fig, ax = plt.subplots(figsize=(11, 8))  # график массы от времени
plt.plot(time, mass, color='indigo', linewidth=4)
ax.set_title("Зависимость массы от времени", fontsize=20)
ax.set_xlabel('Время, с', fontsize=14)
ax.set_ylabel('Масса, кг', fontsize=14)
ax.tick_params(axis='both', which='major', labelsize=14)
formatter = ticker.ScalarFormatter()
formatter.set_scientific(False)
ax.yaxis.set_major_formatter(formatter)
ax.xaxis.set_major_formatter(formatter)
fig.tight_layout()
plt.savefig("графики_ksp/график_массы_от_времени.png")

fig, ax = plt.subplots(figsize=(11, 8))  # график давления от высоты
plt.plot(height, pressure, color='goldenrod', linewidth=4)
ax.set_title("Зависимость давления от высоты", fontsize=20)
ax.set_xlabel('Высота, м', fontsize=14)
ax.set_ylabel('Давление, Па', fontsize=14)
ax.tick_params(axis='both', which='major', labelsize=14)
formatter = ticker.ScalarFormatter()
formatter.set_scientific(False)
ax.yaxis.set_major_formatter(formatter)
ax.xaxis.set_major_formatter(formatter)
fig.tight_layout()
plt.savefig("графики_ksp/график_давления_от_высоты.png")

fig, ax = plt.subplots(figsize=(11, 8))  # график силы тяготения от времени
plt.plot(time, force_of_gravity, color='dimgrey', linewidth=4)
ax.set_title("Зависимость силы тяготения от времени", fontsize=20)
ax.set_xlabel('Время, с', fontsize=14)
ax.set_ylabel('Сила тяготения, Н', fontsize=14)
ax.tick_params(axis='both', which='major', labelsize=14)
formatter = ticker.ScalarFormatter()
formatter.set_scientific(False)
ax.yaxis.set_major_formatter(formatter)
ax.xaxis.set_major_formatter(formatter)
fig.tight_layout()
plt.savefig("графики_ksp/график_силы_тяготения_от_времени.png")

fig, ax = plt.subplots(figsize=(11, 8))  # график плотности воздуха от высоты
plt.plot(height, ro, color='fuchsia', linewidth=4)
ax.set_title("Зависимость плотности воздуха от высоты", fontsize=20)
ax.set_xlabel('Высота, м', fontsize=14)
ax.set_ylabel('Плотность, кг/м^3', fontsize=14)
ax.tick_params(axis='both', which='major', labelsize=14)
formatter = ticker.ScalarFormatter()
formatter.set_scientific(False)
ax.yaxis.set_major_formatter(formatter)
ax.xaxis.set_major_formatter(formatter)
fig.tight_layout()
plt.savefig("графики_ksp/график_плотности_воздуха_от_времени.png")

fig, ax = plt.subplots(figsize=(11, 8))  # график силы тяги двигателей от высоты
plt.plot(time, thrust_of_force, color='lime', linewidth=4)
ax.set_title("Зависимость силы тяги двигателей от времени", fontsize=20)
ax.set_xlabel('Время, с', fontsize=14)
ax.set_ylabel('Сила тяги двигателей, Н', fontsize=14)
ax.tick_params(axis='both', which='major', labelsize=14)
formatter = ticker.ScalarFormatter()
formatter.set_scientific(False)
ax.yaxis.set_major_formatter(formatter)
ax.xaxis.set_major_formatter(formatter)
fig.tight_layout()
plt.savefig("графики_ksp/график_силы_тяги_двигателей_от_высоты.png")

plt.show()