def strictly_ascending(distance: int):
    return [chr for chr in str(distance)] == sorted(set(str(distance)))

def possible_readings(size: int):
    lower_limit, higher_limit = 10 ** (size-1), 9 * int('1' * size)
    return [distance for distance in range(lower_limit, higher_limit) if strictly_ascending(distance) and '0' not in str(distance)]

def next_reading(current_reading: int, readings: list):
    return readings[readings.index(current_reading) + 1]

def prev_reading(current_reading: int, readings: list):
    return readings[readings.index(current_reading) - 1]

def reading_after_n_steps(current_reading: int, steps: int, readings: list):
    return readings[readings.index(current_reading) + steps]

def reading_before_n_steps(current_reading: int, steps: int, readings: list):
    return readings[readings.index(current_reading) - steps]

def step_difference(reading1: int, reading2: int, readings: list):
    return abs(readings.index(reading1) - readings.index(reading2))

readings = possible_readings(3)
print(next_reading(234, readings))
print(prev_reading(234, readings))
print(reading_after_n_steps(234, 2, readings))
print(reading_before_n_steps(234, 2, readings))
print(step_difference(234, 567, readings))