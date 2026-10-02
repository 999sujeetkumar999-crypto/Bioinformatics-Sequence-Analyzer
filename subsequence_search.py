sequence = input("ENETR DNA SEQUENCE: ").upper()

valid_bases = set("ATGC")

if not set(sequence).issubset(valid_bases):
    print("INVALID DNA SEQUENCE!" )
else:

    motifs_input = input("Enter motif(s) separated by comma: ").upper()
    motifs = [motif.strip() for motif in motifs_input.split(",")]

    for motif in motifs:

            if not set(motif).issubset(valid_bases):
        
             print(f"\nInvalid motif: {motif}")
             continue
        
            positions = []

            for i in range(len(sequence) - len(motif) + 1):

             if sequence[i:i + len(motif)] == motif:
                positions.append(i)

            print("\n---------------")
            print("Motif:", motif)

            if positions:
             print("Positions:", positions)
             print("Total occurrences:", len(positions))
            else:
                print("Motif not found")