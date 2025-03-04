# src/data_processing.py
import time
import threading
from collections import deque

temperature_averages = {}  # Global dictionary to store temperature averages
temperature_queue = deque() # Queue to store the temperatures, it works like a list but is thread-safe
lock = threading.RLock() # Reentrant lock for thread safety

def process_temperatures(sensor_ids):
    """
    Continuously calculates the average temperature from readings in the
    temperature_queue and updates the global temperature_averages dictionary.
    """
    global temperature_averages
    while True:
        time.sleep(5) # Wait for 5 seconds
        with lock:
            if temperature_queue:
                temperatures = list(temperature_queue)
                for i in range(len(sensor_ids)):
                    sensor_temps = [temp[1] for temp in temperatures if temp[0] == f'Sensor{i}']
                    if sensor_temps:
                        avg_temp = sum(sensor_temps) / len(sensor_temps)
                        temperature_averages[f'Sensor{i}'] = avg_temp
                    else:
                        temperature_averages[f'Sensor{i}'] = '--'
                temperature_queue.clear()  # Clear the queue after processing

def add_temperature(sensor_id, temperature):
    """
    Adds a temperature to the temperature queue.
    """
    with lock:
        temperature_queue.append((sensor_id, temperature))

# src/sensor_simulation.py
import random
import time
import threading
from src import data_processing

sensor_ids = ["Sensor0", "Sensor1", "Sensor2"]
latest_temperatures = {}  # Global dictionary to store the latest temperatures
lock = threading.RLock()  # Reentrant lock for thread safety

def simulate_sensor(sensor_id):
    """
    Simulates temperature readings from a sensor and updates the global
    latest_temperatures dictionary.
    """
    while True:
        temperature = random.randint(15, 40)  # Generate a random temperature
        with lock:
            latest_temperatures[sensor_id] = temperature  # Update the global dictionary
            data_processing.add_temperature(sensor_id, temperature) # Add temperature to queue
        time.sleep(1)  # Wait for 1 second

# main.py
import threading
import time
from src import sensor_simulation
from src import data_processing
from src import display

def main():
    """
    Main function to start the sensor simulations, data processing, and display.
    """
    # Define the sensor IDs
    sensor_ids = ["Sensor0", "Sensor1", "Sensor2"]

    # Initialize the display
    display.initialize_display(sensor_ids)

    # Create threads for each sensor
    sensor_threads = []
    for sensor_id in sensor_ids:
        thread = threading.Thread(target=sensor_simulation.simulate_sensor, args=(sensor_id,), daemon=True)
        sensor_threads.append(thread)
        thread.start()

    # Create a thread for processing temperatures
    processing_thread = threading.Thread(target=data_processing.process_temperatures, args=(sensor_ids,), daemon=True)
    processing_thread.start()

    # Update the display every second
    try:
        while True:
            display.update_display(sensor_ids)
            time.sleep(1)
    except KeyboardInterrupt:
        print("Exiting the program.")


if __name__ == "__main__":
    main()
