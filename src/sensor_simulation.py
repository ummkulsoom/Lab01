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

