

import matplotlib.pyplot as plt

dna = input("Enter DNA Sequence: ").upper()

valid_bases = set("ATGC")

if set(dna).issubset(valid_bases) and len(dna) > 0:

    print("\n===== GC/AT ANALYSIS =====")

    length = len(dna)

    A = dna.count("A")
    T = dna.count("T")
    G = dna.count("G")
    C = dna.count("C")

    gc_content = ((G + C) / length) * 100
    at_content = ((A + T) / length) * 100

    print("DNA Sequence:", dna)
    print("DNA Length:", length)

    print("\nNucleotide Count:")
    print("A:", A)
    print("T:", T)
    print("G:", G)
    print("C:", C)

    print("\nGC Content:", round(gc_content, 2), "%")
    print("AT Content:", round(at_content, 2), "%")

    
    bases = ["A", "T", "G", "C"]
    counts = [A, T, G, C]

    plt.figure()
    plt.bar(bases, counts)
    plt.title("Nucleotide Count")
    plt.xlabel("Nucleotide")
    plt.ylabel("Count")
    plt.savefig("nucleotide_count.png")
    plt.show()

  
    contents = [gc_content, at_content]
    labels = ["GC", "AT"]

    plt.figure()
    plt.pie(contents, labels=labels, autopct="%1.1f%%")
    plt.title("GC vs AT Content")
    plt.savefig("gc_at_pie.png")
    plt.show()

    # 3. Sequence length distribution
    plt.figure()
    plt.hist([length], bins=5)
    plt.title("Sequence Length Distribution")
    plt.xlabel("Sequence Length")
    plt.ylabel("Frequency")
    plt.savefig("sequence_length_distribution.png")
    plt.show()

else:
    print("Invalid DNA sequence!")