from Bio import Entrez, SeqIO
from io import StringIO




Entrez.email = "999sujeetkumar999@gmail.com"

print("\n===== REAL BIOLOGICAL DATA =====")



accession = input("Enter NCBI Accession ID: ").strip()



try:

    handle = Entrez.efetch(
        db="nuccore",
        id=accession,
        rettype="fasta",
        retmode="text"
    )

    data = handle.read()
    handle.close()


    

    fasta_start = data.find(">")

    if fasta_start == -1:

        print("\nERROR: NCBI did not return a FASTA sequence.")
        print(data[:500])
        exit()

    fasta_data = data[fasta_start:]


    record = SeqIO.read(
        StringIO(fasta_data),
        "fasta"
    )


  

    print("\n===== SEQUENCE INFORMATION =====")

    print("Sequence ID:", record.id)

    print("Description:", record.description)

    print("Sequence Length:", len(record.seq))


 
    print("\nDNA Sequence:")

    print(record.seq)


 
    gc_count = (
        record.seq.count("G")
        + record.seq.count("C")
    )

    gc_content = (
        gc_count / len(record.seq)
    ) * 100


    print(
        "\nGC Content:",
        round(gc_content, 2),
        "%"
    )



except Exception as e:

    print("\nERROR:", e)