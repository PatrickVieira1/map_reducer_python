# map_reducer.py

"""
This script implements a basic map-reduce functionality.

The main purpose of this script is to demonstrate how the map-reduce paradigm can be implemented in Python.

The script takes a list of input data and applies a map function to each element of the list. The map function transforms each element into a key-value pair.

After the map phase, the script performs a reduce operation on the key-value pairs. The reduce function aggregates the values associated with each key.

The input data and the map and reduce functions are defined in the script.

Usage:
    python map_reducer.py

Author: [Your Name]
Date: [Current Date]
"""

# Define the input data
data = [1, 2, 3, 4, 5]

# Define the map function
def map_function(element):
    """
    Maps an element to a key-value pair.

    Args:
        element: The input element.

    Returns:
        A tuple containing the key-value pair.
    """
    return element, element * 2

# Define the reduce function
def reduce_function(key, values):
    """
    Reduces the values associated with a key.

    Args:
        key: The key.
        values: A list of values associated with the key.

    Returns:
        The reduced value.
    """
    return sum(values)

# Perform the map phase
mapped_data = [map_function(element) for element in data]

# Perform the reduce phase
reduced_data = {}
for key, value in mapped_data:
    if key in reduced_data:
        reduced_data[key].append(value)
    else:
        reduced_data[key] = [value]

# Print the result
for key, values in reduced_data.items():
    print(f"{key}: {reduce_function(key, values)}")

