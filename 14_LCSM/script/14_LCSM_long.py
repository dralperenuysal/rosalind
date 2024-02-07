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

def motif_producer(motif, k):
    list = []
    for i in range(0, len(motif) - k + 1):
        if len(motif[i:i + k]) == k:  # Bu kontrol aslında artık gereksiz, ama isteğe bağlı olarak kalabilir
            list.append(motif[i:i + k])
    return list

def find_shortest(sequences):
    """Given a dictionary of sequences, returns the length of the shortest sequence as an integer."""
    # Eğer sequences boş ise, direkt olarak 0 döndür
    if not sequences:
        return 0
    # Sözlükteki tüm dizilerin uzunluklarını bir liste içinde topla
    lengths = [len(seq) for seq in sequences.values()]
    # Bu uzunluklardan en kısa olanını bul ve döndür
    return min(lengths)
def find_longest_common_motif(sequences):
    # En kısa dizinin uzunluğunu bul (k)
    k = find_shortest(sequences)

    # k'nın 2'ye düşene kadar veya ortak bir motif bulana kadar döngü
    while k > 1:
        # Tüm olası motifleri saklayacak bir sözlük
        all_motifs = {}
        for seq_id, seq in sequences.items():
            motifs = motif_producer(seq, k)
            for motif in motifs:
                if motif in all_motifs:
                    all_motifs[motif].add(seq_id)
                else:
                    all_motifs[motif] = {seq_id}

        # Tüm dizilerde ortak olan motifleri bul
        common_motifs = [motif for motif, ids in all_motifs.items() if len(ids) == len(sequences)]

        # Eğer ortak motif varsa, bunlardan birini döndür
        if common_motifs:
            return common_motifs[0]  # Ortak motiflerden ilkini döndür

        # Ortak motif bulunamadıysa, k'yı azalt ve devam et
        k -= 1

    # Ortak motif bulunamadı
    return "No common motif found"

import os
os.getcwd()
seqs = read_data("12_GRAPH/resource/rosalind_grph.txt")
longest = find_longest_common_motif(seqs)