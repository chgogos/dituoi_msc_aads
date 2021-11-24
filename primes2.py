import sys
import time

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    r = int(n ** 0.5)
    i = 5
    while i <= r:
        if n % i == 0:
            return False
        i += 2
    return True


if len(sys.argv) == 3:
    from_ = int(sys.argv[1])
    to = int(sys.argv[2])
else:
    from_ = 1
    to = 100_000

start = time.time() 
c = 0
for x in range(from_, to + 1):
    if is_prime(x):
        c += 1
        
time_elapsed = time.time() - start
print(f"Το πλήθος των πρώτων αριθμών από {from_} μέχρι και {to} είναι {c}")
print(f"Time elapsed =  {time_elapsed:.2f}seconds")