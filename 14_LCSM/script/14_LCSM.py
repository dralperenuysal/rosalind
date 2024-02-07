from Bio import SeqIO
def read_data(file_path):
    """FASTA formatındaki dosyadan sekansları okur ve bir sözlük olarak döndürür."""
    sequences = {record.id:str(record.seq) for record in SeqIO.parse(file_path, "fasta")}
    return sequences

def find_longest_common_motif(sequences):
    from itertools import combinations

    def common_substring_finder(strs):
        """Verilen string listesindeki en uzun ortak alt stringi bulur."""
        shortest_str = min(strs, key=len)
        for length in range(len(shortest_str), 1, -1):
            for start in range(len(shortest_str) - length + 1):
                substr = shortest_str[start:start+length]
                if all(substr in other for other in strs):
                    return substr
        return ""

    return common_substring_finder(sequences.values()) or "No common motif found"

seqs = read_data("14_LCSM/resource/rosalind_lcsm.txt")
find_longest_common_motif(seqs)
