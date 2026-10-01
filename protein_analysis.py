
protein = input("Enter Protein Sequence: ").upper()

valid_amino_acids = set("ARNDCEQGHILKMFPSTWYV")

if set(protein).issubset(valid_amino_acids) and len(protein) > 0:

    print("\n===== PROTEIN SEQUENCE ANALYSIS =====")

    length = len(protein)

    print("Protein Sequence:", protein)
    print("Protein Length:", length)

    # Amino acid counting
    amino_acids = {}

    for amino_acid in protein:
        if amino_acid in amino_acids:
            amino_acids[amino_acid] += 1
        else:
            amino_acids[amino_acid] = 1

    # Amino acid composition
    print("\nAmino Acid Composition:")

    for amino_acid, count in amino_acids.items():
        percentage = (count / length) * 100
        print(
            amino_acid,
            ":",
            count,
            "(",
            round(percentage, 2),
            "%)"
        )

    # Molecular weight
    molecular_weights = {
        "A": 89.09, "R": 174.20, "N": 132.12,
        "D": 133.10, "C": 121.16, "E": 147.13,
        "Q": 146.15, "G": 75.07, "H": 155.16,
        "I": 131.17, "L": 131.17, "K": 146.19,
        "M": 149.21, "F": 165.19, "P": 115.13,
        "S": 105.09, "T": 119.12, "W": 204.23,
        "Y": 181.19, "V": 117.15
    }

    molecular_weight = 0

    for amino_acid in protein:
        molecular_weight += molecular_weights[amino_acid]

    print("\nApproximate Molecular Weight:",
          round(molecular_weight, 2), "Da")

    # Basic properties
    acidic = protein.count("D") + protein.count("E")
    basic = protein.count("K") + protein.count("R") + protein.count("H")

    print("Acidic Residues:", acidic)
    print("Basic Residues:", basic)

    if basic > acidic:
        print("Overall Property: Basic")
    elif acidic > basic:
        print("Overall Property: Acidic")
    else:
        print("Overall Property: Neutral")

else:
    print("Invalid protein sequence!")