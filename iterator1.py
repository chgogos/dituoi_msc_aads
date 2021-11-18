c = ["nikos", "maria", "petros", "sofia"]
itr = iter(c)

while True:
    try:
        print(next(itr))
    except StopIteration:
        break