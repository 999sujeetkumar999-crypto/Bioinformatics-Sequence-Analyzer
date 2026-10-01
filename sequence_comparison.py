
from Bio import pairwise2

seq1 = input("Enter First DNA Sequence: ").upper()
seq2 = input("Enter Second DNA Sequence: ").upper()

valid_bases = set("ATGC")

if not set(seq1).issubset(valid_bases) or not set(seq2).issubset(valid_bases):

    print("Invalid DNA sequence!")

else:

    print("\n===== SEQUENCE COMPARISON =====")

    print("Sequence 1:", seq1)
    print("Sequence 2:", seq2)

    
    minimum_length = min(len(seq1), len(seq2))

    matches = 0

    for i in range(minimum_length):
        if seq1[i] == seq2[i]:
            matches += 1

    similarity = (matches / minimum_length) * 100

    print("\nMatches:", matches)
    print("Similarity / Identity:",
          round(similarity, 2), "%")

    
    hamming_distance = 0

    for i in range(minimum_length):
        if seq1[i] != seq2[i]:
            hamming_distance += 1

    hamming_distance += abs(len(seq1) - len(seq2))

    print("Hamming Distance:", hamming_distance)

    # Global alignment
    global_alignment = pairwise2.align.globalxx(seq1, seq2)

    print("\n===== GLOBAL ALIGNMENT =====")

    print(pairwise2.format_alignment(*global_alignment[0]))

    # Local alignment
    local_alignment = pairwise2.align.localxx(seq1, seq2)

    print("\n===== LOCAL ALIGNMENT =====")

    print(pairwise2.format_alignment(*local_alignment[0]))
      
 