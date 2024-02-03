import os
print(os.getcwd())

resource = "../resource/rosalind_grph.txt"

def data_reader(file_path):
    """
    Reads a FASTA format file and returns its content as a dictionary.
    Each '>' character starts a new key, with following lines as its value until the next '>'.

    Args:
    file_path (str): The path of the file to be read.

    Returns:
    dict: A dictionary containing the key-value pairs from the file, where the key is the line starting with '>'
    and the value is a concatenation of the following lines until the next key.
    """
    with open(file_path, 'r') as file:
        sequences = {}
        key = None
        for line in file:
            line = line.strip()
            if line.startswith('>'):
                key = line[1:]  # Remove '>' and use the rest as key
                sequences[key] = []  # Initialize a list to hold the sequence lines
            elif key:
                sequences[key].append(line)  # Add this line to the list of lines for the current key

        # Concatenate lines for each key to form single string values
        for key in sequences:
            sequences[key] = ''.join(sequences[key])

    return sequences

def overlap_finder(seq1, seq2, k):
    """Checks if there is an overlap of a specific length between two sequences."""
    return seq1[-k:] == seq2[:k]

def find_all_overlaps(dictionary, k):
    """Finds all overlaps of a specific length 'k' among the items in the dictionary and prints the keys of overlapping pairs."""
    keys = list(dictionary.keys())
    n = len(keys)

    for i in range(n):
        for j in range(n):
            if i != j:  # Prevent comparing the sequence with itself
                seq1 = dictionary[keys[i]]
                seq2 = dictionary[keys[j]]
                if overlap_finder(seq1, seq2, k):
                    print(f"{keys[i]} {keys[j]}")

# Example Dictionary
dictionary = data_reader(resource)

# Calling the Function
k = 3  # The length of overlap to look for
find_all_overlaps(dictionary, k)

