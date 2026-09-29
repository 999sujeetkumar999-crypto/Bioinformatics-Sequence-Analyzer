dna = input("Enetr DNA Sequence: ").upper()

valid_bases = set("ATGC")
if set(dna).issubset(valid_bases):

    print("\n=======DNA TO PROTEIN TRANSLATION=======")

    codon_table = {
        "TTA": "F", "TTC": "F",
        "TTA": "L", "TTG": "L",
        "CTT": "L", "CTC": "L",
        "CTA": "L", "CTG": "L",
        "ATT": "I", "ATC": "I",
        "ATA": "I", "ATG": "M",
        "GTT": "V", "GTC": "V",
        "GTA": "V", "GTG": "V",
        "TCT": "S", "TCC": "S",
        "TCA": "S", "TCG": "S",
        "CCT": "P", "CCC": "P",
        "CCA": "P", "CCG": "P",
        "ACT": "T", "ACC": "T",
        "ACA": "T", "ACG": "T",
        "GCT": "A", "GCC": "A",
        "GCA": "A", "GCG": "A",
        "TAT": "Y", "TAC": "Y",
        "TAA": "*", "TAG": "*",
        "CAT": "H", "CAC": "H",
        "CAA": "Q", "CAG": "Q",
        "AAT": "N", "AAC": "N",
        "AAA": "K", "AAG": "K",
        "GAT": "D", "GAC": "D",
        "GAA": "E", "GAG": "E",
        "TGT": "C", "TGC": "C",
        "TGA": "*", "TGG": "W",
        "CGT": "R", "CGC": "R",
        "CGA": "R", "CGG": "R",
        "AGT": "S", "AGC": "S",
        "AGA": "R", "AGG": "R",
        "GGT": "G", "GGC": "G",
        "GGA": "G", "GGG": "G"

    }

    protein = ""
    for i in range(0,len(dna) -2,3 ):
        codon = dna[i:i+3]
        amino_acid = codon_table[codon]

        if amino_acid == "*":
            break 

        protein += amino_acid

        print("DNA SEQUENCE:",dna)
        print("PROTEIN SEQUENCE:", protein)
        print("PROTEIN LENGTH:", len(protein))

    else:
        print("Invalid DNA Sequence!")