c = ["Nikolaos", "Maria", "Petros", "Sofia"]

# διάσχιση λίστας με iterator
itr = iter(c)
while True:
    try:
        print(next(itr))
    except StopIteration:
        break

print("#" * 20)

# απόκρυψη του iterator
for x in c:
    print(x)

# Nikolaos
# Maria
# Petros
# Sofia
# ####################
# Nikolaos
# Maria
# Petros
# Sofia
