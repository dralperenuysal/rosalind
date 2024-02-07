from Bio import SeqIO

def read_data(file_path):
    """Reads sequences from a FASTA format file and returns them as a dictionary."""
    # This creates a dictionary comprehension that reads the file using SeqIO.parse,
    # setting each sequence's ID as the key and the sequence itself as the value.
    sequences = {record.id:str(record.seq) for record in SeqIO.parse(file_path, "fasta")}
    return sequences

def find_longest_common_motif(sequences):
    from itertools import combinations

    def common_substring_finder(strs):
        """Finds the longest common substring among a list of strings."""
        # Find the shortest string as the common substring must be within it
        shortest_str = min(strs, key=len)
        # Iterate over all possible substring lengths, starting from the longest
        for length in range(len(shortest_str), 1, -1):
            # Iterate over all possible starting points for substrings of the current length
            for start in range(len(shortest_str) - length + 1):
                substr = shortest_str[start:start+length]
                # Check if the current substring is present in all other strings
                if all(substr in other for other in strs):
                    return substr
        return ""

    # Try to find the longest common motif, return it or "No common motif found" if there isn't one
    return common_substring_finder(sequences.values()) or "No common motif found"

input = "14_LCSM/resource/rosalind_lcsm.txt"

seqs = read_data(input)
find_longest_common_motif(seqs)