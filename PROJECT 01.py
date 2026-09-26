
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

at_content = ((a+t)/length)* 100

print("AT Content:", round(at_content,2),"%" )

rna = sequence.replace("T" , "U")
print("RNA:", rna)

complement = ""
for base in sequence:

    if base == "A":
        complement += "T"

    elif base == "T":
        complement += "A"    

    elif base == "G":
             complement += "C"

    elif base == "C":
             complement += "G"


reverse_complement = complement[::-1]

print("Reverse Compliment:", reverse_complement)

valid_bases = set("ATGC")

if set(sequence).issubset(valid_bases):
      print("Valid DNA Sequence")
else:
      print("Invalid DNA Sequence")   

      
     
