import matplotlib.pyplot as plt

dna =  input ("Enter DNA Sequence").upper()

#validate DNA SEQUENCE
valid_bases = set("ATGC")

if set(dna).issubset(valid_bases):

    length = len(dna)

    # Count bases
    A = dna.count("A")
    T = dna.count("T")
    G = dna.count("G")
    C = dna.count("C")

    # Calculate percentages
    gc_content = ((G + C) / length) * 100
    at_content = ((A + T) / length) * 100

    print("\n===== GC/AT ANALYSIS =====")
    print("DNA Sequence:", dna)
    print("DNA Length:", length)
    
    print("\nBase Count:")
    print("A:", A)
    print("T:", T)
    print("G:", G)
    print("C:", C)

    print("\nGC Content:", round(gc_content, 2), "%")
    print("AT Content:", round(at_content, 2), "%")

    # Plot
    labels = ["GC Content", "AT Content"]
    values = [gc_content, at_content]

    plt.bar(labels, values)

    plt.title("GC vs AT Content")
    plt.ylabel("Percentage (%)")
    plt.ylim(0, 100)

    plt.show()

else:
    print("Invalid DNA sequence!")