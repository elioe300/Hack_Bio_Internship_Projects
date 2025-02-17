import math
import random

def logistic_function(time, growth_rate, midpoint, L):
    """
    Computes the logistic function value at a given time.
    
    Parameters:
    - time: The current time step.
    - growth_rate: The rate at which the function grows.
    - midpoint: The midpoint where the curve shifts.
    - L: The carrying capacity (maximum value of the function).
    
    Returns:
    - Computed logistic function value at the given time.
    """
    return L / (1 + math.exp(-growth_rate * (time - midpoint)))


def get_80_percent_result(data_frames, index, midpoint):
    """
    Retrieves the logistic function value at 80% of the midpoint time.
    
    Parameters:
    - data_frames: Dictionary containing logistic data.
    - index: Index of the desired DataFrame.
    - midpoint: Midpoint of the logistic curve.
    
    Returns:
    - The logistic function value at 80% of the midpoint time.
    """
    time = int(midpoint * 1.6)  # Calculate the time at 80% beyond midpoint
    return data_frames[f"DataFrame_{index}"][time][1]  # Retrieve the corresponding function value

def logistic_equation(growth_rate, midpoint, L=1, randomize_growth_rate=False, randomize_midpoint=False, iterations=1):
    """
    Generates logistic growth data for a given number of iterations.
    
    Parameters:
    - growth_rate: The rate of growth in the logistic equation.
    - midpoint: The midpoint of the logistic curve.
    - L: The carrying capacity (default is 1).
    - randomize_growth_rate: If True, assigns a random growth rate between 0.10 and 0.80.
    - randomize_midpoint: If True, assigns a random midpoint between 10 and 80.
    - iterations: Number of times to generate data.
    
    Returns:
    - A dictionary containing logistic growth data for each iteration.
    """
    data_frames = {}  # Dictionary to store generated dataframes
    
    for index in range(iterations):  # Loop to generate multiple datasets
        if randomize_growth_rate: 
            growth_rate = random.uniform(0.10, 0.80)  # Assign a random growth rate if enabled
        if randomize_midpoint:
            midpoint = random.randint(10, 80)  # Assign a random midpoint if enabled
        
        data_frame = []  # List to store time-value pairs for logistic function
        for time in range(midpoint * 2):  # Generate values for twice the midpoint time
            data_frame.append([time, logistic_function(time, growth_rate, midpoint, L)])
        
        data_frames[f"DataFrame_{index+1}"] = data_frame  # Store dataframe with unique key
    
    return data_frames
