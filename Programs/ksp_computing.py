from math import *

# Константы и постоянные
G = 6.67 * 10 ** -11  # гравитационная постоянная
g = 9.81  # ускорение свободного падения
T = 300  # температура
M = 0.029  # молярная масса воздуха
R = 8.314  # универсальная газовая постоянна

total_time = 200  # время, с
PK = 101325  # атмосферное давление на поверхности Кербина
radius_of_kerbin = 600000  # радиус Кербина, м
mass_of_kerbin = 5.292 * 10 ** 22  # масса Кербина, кг
initial_mass = 192.6 * 1000  # начальная масса ракеты, кг
empty_mass = 42.11 * 1000  # масса ракеты без топлива, кг
Isp = 302  # удельный импульс двигателей, с
resistance_coefficient = 0.74  # коэффициент лобового аэродинамического сопротивления
S = 1.875  # площадь конуса, м^2

mass_of_side_engine = 5.4 * 1000  # масса каждого отдельного бокового двигателя, кг
mass_of_central_engine = 1.65 * 1000  # масса центрального двигателя, кг
mass_of_maneuverable_engine = 6.6 * 1000  # масса маневорового двигателя, кг
mass_of_side_tank_full = 22.5 * 1000  # масса каждого бака бокового двигателя в наполненном состоянии, кг
mass_of_side_tank_empty = 2.5 * 1000  # масса каждого бака бокового двигателя в сухом состоянии, кг
mass_of_central_bottom_tank_full = 8.5 * 1000  # масса нижнего бака центрального двигателя в наполненном состоянии, кг
mass_of_central_bottom_tank_empty = 1.1 * 1000  # масса нижнего бака центрального двигателя в сухом состоянии, кг
mass_of_central_top_1_tank_full = 14.9 * 1000  # масса верхнего 1 бака центрального двигателя в наполненном состоянии,кг
mass_of_central_top_1_tank_empty = 1.7 * 1000  # масса верхнего 1 бака центрального двигателя в сухом состоянии, кг
mass_of_central_top_2_tank_full = 11.3 * 1000  # масса верхнего 2 бака центрального двигателя в наполненном состоянии,кг
mass_of_central_top_2_tank_empty = 1.4 * 1000  # масса верхнего 2 бака центрального двигателя в сухом состоянии, кг
mass_of_central_top_3_tank_full = 33.6 * 1000  # масса верхнего 3 бака центрального двигателя в наполненном состоянии,кг
mass_of_central_top_3_tank_empty = 3.9 * 1000  # масса верхнего 3 бака центрального двигателя в сухом состоянии, кг
mass_of_maneuverable_tank_full = 4.3 * 1000  # масса бака маневрового двигателя в наполненном состоянии, кг
mass_of_maneuverable_tank_empty = 0.6 * 1000  # масса бака маневрового двигателя в сухом состоянии, кг

stage_periods = [65, 111, 200]
stage_engine_duration = [65, 111, 89]  # время работы двигателей каждой ступени, с


start_mass_on_every_stage = [  # масса ракеты в начале каждой ступени
    initial_mass,
    initial_mass - (mass_of_side_engine + mass_of_side_tank_full) * 4 - 25000,
    initial_mass - (mass_of_side_engine + mass_of_side_tank_full) * 4 - 25000 - 26000,
    initial_mass - (mass_of_side_engine + mass_of_side_tank_full) * 4 - (
            mass_of_central_engine + mass_of_central_bottom_tank_full + mass_of_central_top_1_tank_full +
            mass_of_central_top_2_tank_full + mass_of_central_top_3_tank_full) - (
            mass_of_maneuverable_engine + mass_of_maneuverable_tank_full)]


end_mass_on_every_stage = [  # масса ракеты в конце каждой ступени
    start_mass_on_every_stage[0] - (mass_of_side_tank_full - mass_of_side_tank_empty) * 4 - 25000,
    start_mass_on_every_stage[1] - (mass_of_side_tank_full - mass_of_side_tank_empty) * 4 - 25000 - 26000,
    start_mass_on_every_stage[2] - (mass_of_central_top_1_tank_empty -
                                    mass_of_central_top_2_tank_empty -
                                    mass_of_central_top_3_tank_empty -
                                    mass_of_central_bottom_tank_empty -
                                    mass_of_maneuverable_tank_full -
                                    mass_of_maneuverable_tank_empty),
    start_mass_on_every_stage[3]]


def fuel_consumption_coefficient(mass_with_fuel, mass_without_fuel, time_of_work):  # формула расчета коэффицента расхода топлива, кг в секунду
    return (mass_with_fuel - mass_without_fuel) / time_of_work


fuel_consumption_coefficient_values = [
    fuel_consumption_coefficient(mass_of_side_tank_full * 4 + mass_of_central_top_1_tank_full + mass_of_central_top_2_tank_full +
                                 mass_of_central_top_3_tank_full + mass_of_central_bottom_tank_full,
                                 mass_of_side_tank_empty * 4 + 48000 + mass_of_central_top_1_tank_empty + mass_of_central_top_2_tank_empty +
                                 mass_of_central_top_3_tank_empty + mass_of_central_bottom_tank_empty, stage_engine_duration[0]),
    fuel_consumption_coefficient(48000 + mass_of_central_top_1_tank_empty + mass_of_central_top_2_tank_empty +
                                 mass_of_central_top_3_tank_empty + mass_of_central_bottom_tank_empty,
                                 mass_of_central_top_1_tank_empty + mass_of_central_top_2_tank_empty +
                                 mass_of_central_top_3_tank_empty + mass_of_central_bottom_tank_empty,
                                 stage_engine_duration[1]),
    fuel_consumption_coefficient(mass_of_maneuverable_tank_full + 6000,
                                 mass_of_maneuverable_tank_full,
                                 stage_engine_duration[2]),
    0]

fuel_consumption_coefficient_on_stage = [
    fuel_consumption_coefficient_values[0],
    fuel_consumption_coefficient_values[1],
    fuel_consumption_coefficient_values[2],
    0]


def stage(t):  # определение активной ступени
    global stage_periods
    result = 3
    for i in range(len(stage_periods)):
        if stage_periods[i] >= t:
            result = i
            break
    return result


def angle(h):  # определение угла взависимости от высоты
    if h <= 1000:
        return 0
    elif h >= 30000:
        return 50
    return (h - 1000) / (30000 - 1000) * 50


def length_of_vector(v):
    return (v[0] ** 2 + v[1] ** 2) ** 0.5


def drag_force(Cd, velocity_array_in_time, S, ro):  # сила сопротивления воздуха в Ньютонах
    return (Cd * ro * velocity_array_in_time ** 2 * S) / 2


def ro(P, M, R, T):  # плотность воздуха
    return (P * M) / (T * R)


def pressure(PK, M, R, T, g, h):  # атмосферное давление взависимости от высоты
    return (PK * exp(-M * g * h / (R * T)))


def force_of_gravity(G, mass_of_rocket, mass_of_kerbin, distance):  # модуль силы гравитационного взаимодействия, Н
    return (G * mass_of_rocket * mass_of_kerbin) / (distance ** 2)


def mass_of_rocket_in_moment(t):  # масса топлива взависимости от времени на конктретной ступени, кг
    global stage_periods
    global start_mass_on_every_stage
    time_on_stage = t
    if stage(t) > 0:
        time_on_stage -= stage_periods[stage(t) - 1]
    return start_mass_on_every_stage[stage(t)] - fuel_consumption_coefficient_values[stage(t)] * time_on_stage


def scalar_to_vector(scalar, vector):
    distance = length_of_vector(vector)
    if distance == 0:
        return (0, 0)
    cosinus = -vector[0] / distance
    sinus = -vector[1] / distance
    return (scalar * cosinus, scalar * sinus)


def acceleration(force_of_thrust, force_of_gravity, force_of_air_resistance, angle, mass_of_rocket):  # ускорение, м/с^2
    return ((force_of_thrust * cos(radians(angle)) + force_of_gravity[0] + force_of_air_resistance[0]) / mass_of_rocket,
            (force_of_thrust * sin(radians(angle)) + force_of_gravity[1] + force_of_air_resistance[1]) / mass_of_rocket)


def force_of_thrust(Isp, fuel_consumption_coefficient):  # сила тяги двигателя, Н
    return Isp * fuel_consumption_coefficient * g


force_of_thrust_values = [
    force_of_thrust(Isp, fuel_consumption_coefficient_on_stage[0]),
    force_of_thrust(Isp, fuel_consumption_coefficient_on_stage[1]),
    force_of_thrust(Isp, fuel_consumption_coefficient_on_stage[2]),
    0]

position_array = [(radius_of_kerbin, 0)]
height_array = [length_of_vector(position_array[0]) - radius_of_kerbin]
velocity_array = [(0, 0)]
mass_of_rocket_array = [mass_of_rocket_in_moment(t) for t in range(total_time + 1)]

force_of_gravity_array = [force_of_gravity(
    G,
    mass_of_rocket_array[0],
    mass_of_kerbin,
    height_array[0] + radius_of_kerbin)]

time_array = list(range(total_time + 1))
pressure_array = [pressure(PK, M, R, T, force_of_gravity_array[0] / mass_of_rocket_array[0], height_array[0])]
ro_array = [ro(pressure_array[0], M, R, T)]

drag_force_array = [drag_force(
    resistance_coefficient,
    length_of_vector(velocity_array[0]),
    S,
    ro(pressure_array[0], M, R, T))]

force_of_thrust_array = [force_of_thrust_values[stage(t)] for t in range(total_time + 1)]
angel_array = [angle(height_array[0])]

acceleration_array = [acceleration(
    force_of_thrust_values[0],
    scalar_to_vector(force_of_gravity_array[0], position_array[0]),
    scalar_to_vector(drag_force_array[0], velocity_array[0]),
    angel_array[0],
    mass_of_rocket_array[0])]

absolute_mass_error = 500  # абсолютная погрешность массы в нулевой момент времени, кг
relative_mass_error = absolute_mass_error / mass_of_rocket_array[0]  # относительная погрешность массы

absolute_thrust_error = 100  # абсолютная погрешность тяги, Н
relative_thrust_error = absolute_thrust_error / force_of_thrust_array[0]  # относительная погрешность массы

for t in range(total_time):

    force_of_gravity_array.append(force_of_gravity(
        G,
        mass_of_rocket_array[t + 1],
        mass_of_kerbin,
        height_array[t] + radius_of_kerbin))

    pressure_array.append(pressure(
        PK, M, R, T,
        force_of_gravity_array[t] / mass_of_rocket_array[t],
        height_array[t]))

    ro_array.append(ro(pressure_array[t], M, R, T))

    drag_force_array.append(drag_force(
        resistance_coefficient,
        length_of_vector(velocity_array[t]),
        S,
        ro_array[t]))

    velocity_array.append((velocity_array[t][0] + acceleration_array[t][0],
                           velocity_array[t][0] + acceleration_array[t][1]))

    position_array.append((position_array[t][0] + velocity_array[t][0],
                           position_array[t][1] + velocity_array[t][1]))

    height_array.append((length_of_vector(position_array[t]) - radius_of_kerbin) / 1.40)

    angel_array.append(angle(height_array[t]))

    acceleration_array.append(acceleration(
        force_of_thrust_array[t + 1],
        scalar_to_vector(force_of_gravity_array[t], position_array[t]),
        scalar_to_vector(drag_force_array[t], velocity_array[t]),
        angel_array[t],
        mass_of_rocket_array[t]))

velocity_scalar_array = [length_of_vector(velocity_array[i]) for i in range(total_time + 1)]
