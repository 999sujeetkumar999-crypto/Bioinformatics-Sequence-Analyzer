
sequence = input (" Enter a DNA sequence: ").upper()
print("\n--- DNA SEQUENCE ANALYZER ---")
length = len(sequence)
print("Sequence length:", length)

a = sequence.count("A")
t = sequence.count("T")
g = sequence.count("G")
c = sequence.count("C")

print("A:" , a)
print("T:" , t)
print("G:" , g)
print("C:" , c)

gc_content = ((g+c)/length)* 100

print("GC Content:", round(gc_content,2),"%")

