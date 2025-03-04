# src/display.py
import os
import time
from src import sensor_simulation
from src import data_processing

def initialize_display(sensor_ids):
    """
    Prints the initial layout for displaying temperatures.
    """
    print("Current temperatures:")
    print("Latest Temperatures: " + " ".join([f"Sensor {i}: --°C" for i in range(len(sensor_ids))]))
    for i in range(len(sensor_ids)):
        print(f"Sensor {i+1} Average: --°C")

def update_display(sensor_ids):
    """
    Refreshes the latest temperatures and averages in place on the console
    without erasing the console.
    """
    os.system('clear') # Clear the screen

    # Print latest temperatures
    print("Current temperatures:")
    latest_temps = " ".join([f"Sensor {i}: {sensor_simulation.latest_temperatures.get(f'Sensor{i}', '--')}°C" for i in range(len(sensor_ids))])
    print("Latest Temperatures: " + latest_temps)

    # Print average temperatures
    for i in range(len(sensor_ids)):
        avg_temp = data_processing.temperature_averages.get(f'Sensor{i}', '--')
        if isinstance(avg_temp, (int, float)):
            avg_temp_str = f"{avg_temp:.2f}"
        else:
            avg_temp_str = avg_temp  # Use the string '--' directly
        print(f"Sensor {i+1} Average: {avg_temp_str}°C")
