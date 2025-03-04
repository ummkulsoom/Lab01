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
