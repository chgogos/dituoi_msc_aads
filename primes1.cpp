#include <iostream>
#include <chrono>

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
