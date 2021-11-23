def is_prime(n):
    if n in [2, 3, 5, 7]:
        return True
    if n < 2 or n % 2 == 0 or n % 3 == 0:
        return False
    r = int(n ** 0.5)
    # όλοι οι πρώτοι > 3 είναι της μορφής 6i + 1 ή 6i - 1
    # ξεκινάμε με i = 5 (που είναι πρώτος)
    # και ελέγχουμε i, i + 2 για το αν είναι πρώτοι
    # η επανάληψη συνεχίζεται με βήμα 6
    i = 5
    while i <= r:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


from_ = 1
to = 1_000_000

c = 0
for x in range(from_, to + 1):
    if is_prime(x):
        c += 1

print(f"Το πλήθος των πρώτων αριθμών από {from_} μέχρι και {to} είναι {c}")
