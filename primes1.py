def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    f = True
    for i in range(2, n):
        if n % i == 0:
            f = False
    return f


from_ = 1
to = 100_000

c = 0
for x in range(from_, to + 1):
    if is_prime(x):
        c += 1

print(f"Το πλήθος των πρώτων αριθμών από {from_} μέχρι και {to} είναι {c}")
