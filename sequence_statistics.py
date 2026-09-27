sequence = input("Enter DNA sequence: ").upper()

length =  len(sequence)

a = sequence.count("A")
t = sequence.count("T")
g = sequence.count("G")
c = sequence.count("C")

purines = a + g
pyrimidines = t + c

purines_percentage = (purines/length) * 100
pyrimidines_percentage = (pyrimidines/length) * 100

at_gc_ratio =  (a+t)/(g+c)

nucleotides = {
      "A": a,
      "T": t,
      "G": g,
      "C": c
}

most_frequent = max(nucleotides, key= nucleotides.get)
least_frequent = min(nucleotides, key= nucleotides.get)

print("\n========== SEQUENCE STATISTICS ==========")

print("Sequence length:",length)

print("\nNucleotide Frequency:")
print("A:", a)
print("T:", t)
print("G:", g)
print("C:", c)

print("\nMost frequent Nucleotide:", most_frequent)
print("Least frequent Nucleotide:", least_frequent) 

print("\nPurines (A + G):",purines)
print("Pyrimidines (T + C):", pyrimidines)

print("Purine Percentage:", round(purines_percentage, 2), "%")
print("Pyrimidine Percentage:", round(pyrimidines_percentage, 2), "%")

print("AT/GC Ratio:", round(at_gc_ratio, 2))

