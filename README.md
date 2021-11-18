# Αλγόριθμοι και Προχωρημένες Δομές Δεδομένων

* [primes1.py](./primes1.py)
* [primes2.py](./primes2.py)
* [primes3.py](./primes3.py)

* [primes1.cpp](./primes1.cpp)

```
> g++ primes1.cpp -o primes1.exe
> Measure-Command {.\primes1.exe | Out-Default}
...
TotalSeconds      : 10,3607604
...
```

* [primes2.cpp](./primes2.cpp)

```
> g++ primes2.cpp -o primes2.exe -O3
> Measure-Command {.\primes2.exe | Out-Default}
...
TotalSeconds      : 0,093944
...