sequence = input("Enter DNA sequence: ")

sequence = sequence.upper()

print("Sequence:", sequence)
print("Length:", len(sequence))

print("A:", sequence.count("A"))
print("T:", sequence.count("T"))
print("G:", sequence.count("G"))
print("C:", sequence.count("C"))

gc_count = sequence.count("G") + sequence.count("C")
gc_content = (gc_count / len(sequence)) * 100

print("GC Content:", gc_content, "%")