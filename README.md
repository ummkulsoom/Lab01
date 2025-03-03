Sequential Execution: 
The sequential approach had the longest execution time as each hyperparameter combination was evaluated one by one.
Threaded Execution: 
Threading reduced execution time by allowing multiple combinations to be evaluated concurrently. However, it still has limitations in CPU-bound tasks.
Multiprocessing Execution: 
Multiprocessing provided the most significant reduction in execution time, as it runs each combination on separate CPU cores, making the process much faster.

In summary, moving from sequential to threaded to multiprocessing execution significantly reduced the execution time, with multiprocessing providing the most efficient parallelization.

Threaded Execution Performance:
Best RMSE: The lowest RMSE value achieved during the hyperparameter search using threading.
Best MAPE: The lowest MAPE value achieved during the hyperparameter search using threading.

Multiprocessing Execution Performance:
Best RMSE: The lowest RMSE value achieved during the hyperparameter search using multiprocessing.
Best MAPE: The lowest MAPE value achieved during the hyperparameter search using multiprocessing.

Key Observations:
Both threading and multiprocessing achieved similar RMSE and MAPE values, as the model training process was the same.
Multiprocessing provided the same performance metrics in a shorter time due to better parallelization, utilizing multiple CPU cores.

The performance metrics (RMSE and MAPE) were almost identical between the threaded and multiprocessing implementations, but multiprocessing was faster.
