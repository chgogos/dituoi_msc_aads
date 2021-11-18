c = ["Nikolaos", "Maria", "Petros", "Sofia"]

itr = iter(c)

while True:
    try:
        print(next(itr))
    except StopIteration:
        break
