import random


def generate_dna_strings(n, m, seed=1):
    """n = πλήθος ακολουθιών DNA, m = πλήθος χαρακτήρων ανά ακολουθία"""
    dna_strings = []

    for i in range(n):
        a_dna = []
        for j in range(m):
            a_dna.append(random.choice(["A", "G", "C", "T"]))
        dna_strings.append("".join(a_dna))
    return dna_strings


dataset = generate_dna_strings(10, 20)
print(dataset)
