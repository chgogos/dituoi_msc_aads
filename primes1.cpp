#include <iostream>

// συνάρτηση ελέγχου του εάν ένας ακέραιος αριθμός είναι πρώτος (αργή έκδοση)
bool is_prime(int x)
{
    if (x <= 1)
        return false;
    if (x <= 3)
        return true;
    bool f = true;
    for (int i = 2; i < x; i++)
        if (x % i == 0)
            f = false;
    return f;
}

int main()
{
    int c = 0;
    int from = 1, to = 100000;
    for (int x = from; x <= to; x++)
        if (is_prime(x))
            c++;
    std::cout << "number of primes between " << from << " and " << to << " are " << c << std::endl;
}
