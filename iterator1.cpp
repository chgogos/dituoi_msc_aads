#include <iostream>
#include <vector>

using namespace std;

int main()
{
    vector<string> v{"Nikolaos", "Maria", "Petros", "Sofia"};
    
    // διάσχιση vector με iterator
    vector<string>::iterator itr = v.begin();
    while (itr != v.end())
    {
        cout << *itr << endl;
        itr++;
    }

    cout << "################################" << endl;

    // απόκρυψη του iterator
    for (const auto &x : v)
    {
        cout << x << endl;
    }
}

// Nikolaos
// Maria
// Petros
// Sofia
// ################################
// Nikolaos
// Maria
// Petros
// Sofia