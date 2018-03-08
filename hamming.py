def distance(strand_a, strand_b):
    if len(strand_a) != len(strand_b):
        raise ValueError("Cannot verify hamming difference. Please check strands are of equal length")
    ham_d = 0
    for nuc1, nuc2 in zip(strand_a, strand_b):
        if nuc1 != nuc2:
            ham_d += 1
    return ham_d
