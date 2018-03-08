def to_rna(dna_strand):
    mapping = {"G": "C",
           "C": "G",
           "T": "A",
           "A": "U"}
    rna_strand = ""
    for nucleotide in dna_strand:
        if nucleotide not in mapping:
            raise ValueError("Not a valid DNA sequence!")
        else:
            rna_strand += mapping[nucleotide]
    return rna_strand

#     rna = list(
#         "G" if x == "C"
#         else "C" if x == "G"
#         else "A" if x == "T"
#         else "U" if x == "A"
#         else x for x in dna_strand)
#     return "".join(rna)

# Try mapping to include ValueError

