import random


def teased_coin(p):
    if random.random() < p:
        return "H"
    else:
        return "T"


N = 1000000
c = 0
for i in range(N):
    if teased_coin(0.8) == "H":
        c += 1

print(c / N)
