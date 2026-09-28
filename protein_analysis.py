protein = input("Enter Protein Sequence: ").upper()

valid_amino_acids = set("ARNDCEQGHILKMFPSTWYV")

if set(protein).issubset(valid_amino_acids):

    print("\n=====PROTEIN ANALYSIS=====")

    length = len(protein)

    print("Protein Sequence:", protein)
    print("Protein Length:", length)

    amino_acids = {}

    for amino_acid in protein:
        if amino_acid in amino_acids:
            amino_acids[amino_acid] += 1
        else:
            amino_acids[amino_acid] = 1

    print("\nAmino Acid Frequency:")

    for amino_acid, count in amino_acids.items():
        percentage = (count / length) * 100
        print(amino_acid, ":", count, "(", round(percentage, 2), "%)")

    most_frequent = max(amino_acids, key=amino_acids.get)
    least_frequent = min(amino_acids, key=amino_acids.get)

    print("\nMost Frequent Amino Acid:", most_frequent)
    print("Least Frequent Amino Acid:", least_frequent)

else:
    print("Invalid protein sequence!")