from scipy.integrate import odeint
import matplotlib.pyplot as plt
import krpc
import os
from matplotlib import ticker
from math import sin

connection = krpc.connect(name='Graphics')
vessel = connection.space_center.active_vessel

speed_ar = []
time_ar = []
altitude_ar = []
pressure_ar = []
initial_mass_ar = []
air_density_ar = []
drag_ar = []
thrust_ar = []
gravity_ar = []
orbit_frame = vessel.orbit.body.reference_frame
body = vessel.orbit.body
 
def f(x):    
    return sin(x)

while True:
        speed_ar.append(vessel.flight(orbit_frame).speed)
        time_ar.append(vessel.met)
        altitude_ar.append(vessel.flight().mean_altitude)
        initial_mass_ar.append(vessel.mass)
        atmosphere = body.has_atmosphere
        air_density_ar.append(body.density_at(vessel.flight().mean_altitude))
        drag_ar.append(vessel.flight().drag)
        thrust_ar.append(vessel.thrust)
        gravity_ar.append(vessel.orbit.body.surface_gravity * vessel.mass)
        if vessel.met > 200:
                break
        elif atmosphere == True:
            pressure_ar.append(body.pressure_at(vessel.flight().mean_altitude))
        elif atmosphere == False:
            pressure_ar.append(0.0)
 


fig, ax = plt.subplots(figsize=(11, 8))  # график скорости от времени
plt.plot(time_ar, speed_ar, color='deepskyblue', linewidth=4)
ax.set_title("Зависимость скорости от времени", fontsize=20)
ax.set_xlabel('Время, с', fontsize=14)
ax.set_ylabel('Скорость, м/с', fontsize=14)
ax.tick_params(axis='both', which='major', labelsize=14)
formatter = ticker.ScalarFormatter()
formatter.set_scientific(False)
ax.yaxis.set_major_formatter(formatter)
ax.xaxis.set_major_formatter(formatter)
fig.tight_layout()

fig, ax = plt.subplots(figsize=(11, 8))  # график высоты от времени
plt.plot(time_ar, altitude_ar, color='indigo', linewidth=4)
ax.set_title("Зависимость высоты от времени", fontsize=20)
ax.set_xlabel('Время, с', fontsize=14)
ax.set_ylabel('Высота, м', fontsize=14)
ax.tick_params(axis='both', which='major', labelsize=14)
formatter = ticker.ScalarFormatter()
formatter.set_scientific(False)
ax.yaxis.set_major_formatter(formatter)
ax.xaxis.set_major_formatter(formatter)
fig.tight_layout()

fig, ax = plt.subplots(figsize=(11, 8))  # график давления от высоты
plt.plot(altitude_ar[1:], pressure_ar, color='darkorange', linewidth=4)
ax.set_title("Зависимость давления от высоты", fontsize=20)
ax.set_xlabel('Высота, м', fontsize=14)
ax.set_ylabel('Давление, Па', fontsize=14)
ax.tick_params(axis='both', which='major', labelsize=14)
formatter = ticker.ScalarFormatter()
formatter.set_scientific(False)
ax.yaxis.set_major_formatter(formatter)
ax.xaxis.set_major_formatter(formatter)
fig.tight_layout()

fig, ax = plt.subplots(figsize=(11, 8))  # график массы от времени
plt.plot(time_ar, initial_mass_ar, color='firebrick', linewidth=4)
ax.set_title("Зависимость массы от времени", fontsize=20)
ax.set_xlabel('Время, с', fontsize=14)
ax.set_ylabel('Масса, кг', fontsize=14)
ax.tick_params(axis='both', which='major', labelsize=14)
formatter = ticker.ScalarFormatter()
formatter.set_scientific(False)
ax.yaxis.set_major_formatter(formatter)
ax.xaxis.set_major_formatter(formatter)
fig.tight_layout()

fig, ax = plt.subplots(figsize=(11, 8))  # график плотности воздуха от высоты
plt.plot(altitude_ar, air_density_ar, color='darkgreen', linewidth=4)
ax.set_title("Зависимость плотности воздуха от высоты", fontsize=20)
ax.set_xlabel('Высота, м', fontsize=14)
ax.set_ylabel('Плотность воздуха, кг/м^3', fontsize=14)
ax.tick_params(axis='both', which='major', labelsize=14)
formatter = ticker.ScalarFormatter()
formatter.set_scientific(False)
ax.yaxis.set_major_formatter(formatter)
ax.xaxis.set_major_formatter(formatter)
fig.tight_layout()

fig, ax = plt.subplots(figsize=(11, 8))  # график силы тяги от времени
plt.plot(time_ar, thrust_ar, color='fuchsia', linewidth=4)
ax.set_title("Зависимость силы тяги от времени", fontsize=20)
ax.set_xlabel('Время, с', fontsize=14)
ax.set_ylabel('Сила тяги, Н', fontsize=14)
ax.tick_params(axis='both', which='major', labelsize=14)
formatter = ticker.ScalarFormatter()
formatter.set_scientific(False)
ax.yaxis.set_major_formatter(formatter)
ax.xaxis.set_major_formatter(formatter)
fig.tight_layout()

fig, ax = plt.subplots(figsize=(11, 8))  # график силы тяготения от времени
plt.plot(time_ar, gravity_ar, color='lime', linewidth=4)
ax.set_title("Зависимость силы тяготения от времени", fontsize=20)
ax.set_xlabel('Время, с', fontsize=14)
ax.set_ylabel('Сила тяготения, Н', fontsize=14)
ax.tick_params(axis='both', which='major', labelsize=14)
formatter = ticker.ScalarFormatter()
formatter.set_scientific(False)
ax.yaxis.set_major_formatter(formatter)
ax.xaxis.set_major_formatter(formatter)
fig.tight_layout()

plt.show()
