sequences = {}

with open("sample.fasta", "r") as file:
    current_id= ""

    for line in file:
        line = line.strip()

        if line.startswith(">"):
            current_id = line[1:]
            sequences[current_id] = ""
        else:
            sequences[current_id] += line   

for seq_id, sequence in sequences.items():
     print("ID:", seq_id)
     print("Sequence:", sequence)
     print("Length:", len(sequence))
     print()          
  