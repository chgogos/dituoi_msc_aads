#include <iostream>
#include <chrono>

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

int main(int argc, char *argv[])
{
    int from = 1, to = 100000;
    if (argc == 3)
    {
        from = atoi(argv[1]);
        to = atoi(argv[2]);
    }
    auto start = std::chrono::high_resolution_clock::now();
    int c = 0;
    for (int x = from; x <= to; x++)
        if (is_prime(x))
            c++;

    auto end = std::chrono::high_resolution_clock::now();
    std::chrono::duration<float> duration = end - start;
    std::cout << "Number of primes between " << from << " and " << to << " are " << c << std::endl;
    std::cout << "Time passed: " << duration.count() << "seconds" << std::endl;
}
