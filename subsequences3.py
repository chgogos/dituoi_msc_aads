from itertools import combinations


def all_subsequences(s):
    out = set()
    for r in range(1, len(s) + 1):
        for c in combinations(s, r):
            out.add("".join(c))
    return sorted(out)


subsequences = all_subsequences("HELLO")
print(subsequences)
