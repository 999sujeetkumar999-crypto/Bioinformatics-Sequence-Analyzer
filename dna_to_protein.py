from Bio.Seq import Seq



dna = input("Enter DNA Sequence: ").upper().strip()

valid_bases = set("ATGC")


if not set(dna).issubset(valid_bases):
    print("Invalid DNA Sequence!")
    exit()

print("\n===== DNA TO PROTEIN TRANSLATION =====")



sequence = Seq(dna)

protein = sequence.translate(to_stop=True)

print("DNA Sequence:", dna)
print("Protein Sequence:", protein)
print("Protein Length:", len(protein))



print("\n===== READING FRAMES =====")

for frame in range(3):

    frame_dna = dna[frame:]

    # Remove incomplete codon
    usable_length = len(frame_dna) - (len(frame_dna) % 3)
    frame_dna = frame_dna[:usable_length]

    frame_protein = Seq(frame_dna).translate(to_stop=True)

    print("\nReading Frame +", frame + 1)
    print("DNA:", frame_dna)
    print("Protein:", frame_protein)




print("\n===== ORF ANALYSIS =====")

start_position = dna.find("ATG")

if start_position != -1:

    orf_dna = dna[start_position:]

    orf_protein = Seq(orf_dna).translate(to_stop=True)

    print("Start Codon ATG found at position:", start_position)
    print("ORF DNA:", orf_dna)
    print("ORF Protein:", orf_protein)
    print("ORF Protein Length:", len(orf_protein))

else:

    print("No start codon ATG found.")