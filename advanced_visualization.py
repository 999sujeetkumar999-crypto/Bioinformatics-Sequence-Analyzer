import matplotlib.pyplot as plt
import seaborn as sns
from collections import Counter


print("===== ADVANCED VISUALIZATION =====")

sequences = [
    "ATGCGTACGATCGATCG",
    "ATGCGCGATATCGATCG",
    "ATATCGCGCGATATGC",
    "GCGCGATATATCGCGC",
    "ATGATCGCGTACGTAGC"
]
gc_contents = []

for sequence in sequences:

    gc_count = sequence.count("G") + sequence.count("C") 
    gc_content = (gc_count / len(sequence)) * 100
    gc_contents.append(gc_content)

plt.figure()

plt.hist(gc_contents, bins=5)

plt.title("GC Content Distribution")

plt.xlabel("GC Content (%)")

plt.ylabel("Number of Sequences")

plt.savefig("gc_content_distribution.png")

plt.show()

lengths = []

for sequences in sequence:
    lengths.append(len(sequence))

plt.figure()

plt.hist(gc_contents, bins=5)

plt.title("GC Content Distribution")

plt.xlabel("GC Content (%)")

plt.ylabel("Number of Sequences")

plt.savefig("gc_content_distribution.png")

plt.show()

protein = "MKTAYIAKQRQISFVKSHFSRQ"

aa_count = Counter(protein)

plt.figure()
plt.bar(
    aa_count.keys(),
    aa_count.values()
)

plt.title("Amino Acid Composition")

plt.xlabel("Amino Acid")

plt.ylabel("Frequency")

plt.savefig("amino_acid_composition.png")

plt.show()

similarity_matrix = [
    [1.00, 0.88, 0.75, 0.70, 0.82],
    [0.88, 1.00, 0.78, 0.72, 0.85],
    [0.75, 0.78, 1.00, 0.80, 0.76],
    [0.70, 0.72, 0.80, 1.00, 0.74],
    [0.82, 0.85, 0.76, 0.74, 1.00]
]

plt.figure()

sns.heatmap(
    similarity_matrix,
    annot=True,
    fmt=".2f"
)

plt.title("Sequence Similarity Heatmap")

plt.xlabel("Sequences")

plt.ylabel("Sequences")

plt.savefig("sequence_similarity_heatmap.png")

plt.show()


print("\nAll visualizations generated successfully!")