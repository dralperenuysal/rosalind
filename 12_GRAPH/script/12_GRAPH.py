def read_data(file_path):
    """Reads a FASTA format file and returns its content as a dictionary."""
    sequences = {}
    key = None
    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip()
            if line.startswith('>'):
                key = line[1:]
                sequences[key] = []
            elif key:
                sequences[key].append(line)
        sequences = {k: ''.join(v) for k, v in sequences.items()}
    return sequences

def overlap_finder(seq1, seq2, k):
    """Checks if there is an overlap of a specific length between two sequences."""
    return seq1[-k:] == seq2[:k]

def find_all_overlaps_and_save(dictionary, k, input_file_path):
    """Finds all overlaps of a specific length 'k' among the items in the dictionary and saves them to a file."""
    output_file_path = "../output/12_GRAPH_output.txt"  # Generate output file name
    keys = list(dictionary.keys())
    overlaps = [(keys[i], keys[j]) for i in range(len(keys)) for j in range(len(keys))
                if i != j and overlap_finder(dictionary[keys[i]], dictionary[keys[j]], k)]

    with open(output_file_path, 'w') as output_file:
        for pair in overlaps:
            output_file.write(f"{pair[0]} {pair[1]}\n")
    print(f"Overlaps saved to {output_file_path}")

# Example usage
resource = "../resource/rosalind_grph.txt"
dictionary = read_data(resource)
k = 3
find_all_overlaps_and_save(dictionary, k, resource)

