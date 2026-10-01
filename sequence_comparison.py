seq1 = input ("Enter First DNA Sequence: ").upper()
seq2 = input("Enter Second DNA Sequence: ").upper()

valid_bases = set("ATGC")

if not set(seq1).issubset(valid_bases) or not set(seq2).issubset(valid_bases):
 print("Invalid DNA sequence!")

elif len(seq1) != len(seq2):
 print("Error: Both sequence must have the same length!")

else:
    matches = 0
    mismatches = 0

    for i in range(len(seq1)):
       if seq1[i] == seq2[i]:
            matches += 1
    else:
            mismatches += 1

    similarity = (matches / len(seq1)) * 100

    print("\n--- Sequence Comparison Result ---")
    print("Sequence 1:", seq1)
    print("Sequence 2:", seq2)
    print("Matches:", matches)
    print("Mismatches:", mismatches)
    print("Similarity:", similarity, "%")
       
      
 