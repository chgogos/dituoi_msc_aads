#include <iostream>

// συνάρτηση ελέγχου του εάν ένας ακέραιος αριθμός είναι πρώτος
bool is_prime(int n)
{
    if (n == 2 || n == 3 || n == 5 || n == 7)
        return true;
    if (n < 2 || n % 2 == 0 || n % 3 == 0)
        return false;
    for (int i = 5; i * i <= n; i += 6)
        if (n % i == 0 || n % (i + 2) == 0)
            return false;
    return true;
}

int main()
{
    int c = 0;
    int from = 1, to = 1000000;
    for (int x = from; x <= to; x++)
        if (is_prime(x))
            c++;
    std::cout << "number of primes between " << from << " and " << to << " are " << c << std::endl;
}
