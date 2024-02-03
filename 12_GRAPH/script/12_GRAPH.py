import os
print(os.getcwd())

resource = "resource/12_GRAPH.txt"

def data_reader(filepath):
    """
    Reads the .txt file at the given file path and returns its content as a dictionary.
    Every two lines in the file are considered a key-value pair.

    Args:
    filepath (str): The path of the file to be read

    Returns:
    dict: A dictionary containing the key-value pairs read from the file

    """
    dictionary = {}  # Compose a blank dict
    with open(filepath, 'r') as file:
        while True:
            key = file.readline().strip()[1:]  # Read the key and delete the spaces
            value = file.readline().strip()  # Read the value and delete the spaces
            if not key or not value:  # If key or value are blank, code exits
                break
            dictionary[key] = value  # Add the data to the dictionary
    return dictionary

def overlap_finder(seq1, seq2, k):
    """Checks if there is an overlap of a specific length between two sequences."""
    return seq1[-k:] == seq2[:k]

def find_all_overlaps(dictionary, k):
    """Finds all overlaps of a specific length 'k' among the items in the dictionary and prints the keys of overlapping pairs."""
    keys = list(dictionary.keys())  # Convert dictionary keys to a list for indexed access
    n = len(keys)  # Number of items in the dictionary

    for i in range(n):
        for j in range(i + 1, n):  # Compare each item with every other item
            seq1 = dictionary[keys[i]]
            seq2 = dictionary[keys[j]]
            if overlap_finder(seq1, seq2, k):  # Check for overlap from seq1 to seq2
                print(f"{keys[i]} and {keys[j]}")
            if overlap_finder(seq2, seq1, k):  # Check for overlap from seq2 to seq1
                print(f"{keys[j]} {keys[i]}")

# Example Dictionary
dictionary = data_reader(resource)

# Calling the Function
k = 3  # The length of overlap to look for
find_all_overlaps(dictionary, k)

