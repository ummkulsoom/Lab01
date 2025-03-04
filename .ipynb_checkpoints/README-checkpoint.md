For synchronization in this project, we used locks (specifically, threading.RLock) to ensure thread safety when accessing shared resources. This was crucial for preventing race conditions and ensuring that data was updated consistently across different threads.

Locks for Sensor Simulations: We used a lock in the simulate_sensor function to ensure that the latest temperatures were updated atomically.

Locks for Data Processing: We used a lock in the process_temperatures function to ensure that the temperature queue was accessed safely and that averages were calculated correctly.