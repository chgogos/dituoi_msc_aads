from subsequences1 import all_subsequences

x = "AATCGAG"
y = "CCATCGG"

x_subseqs = all_subsequences(x)
y_subseqs = all_subsequences(y)

print(x_subseqs)
print(y_subseqs)

m = 0
ms = "NOT FOUND"
for sx in x_subseqs:
    for sy in y_subseqs:
        if sx == sy:
            if len(sx) > m:
                m = len(sx)
                ms = sx

print(f"MAX SUBSEQUENCE = {ms} LENGTH = {m}")
