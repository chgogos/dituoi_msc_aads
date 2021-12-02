#include <iostream>
#include <vector>
#include <algorithm>
#include <numeric>
#include <string>

using namespace std;

int main(int argc, char *argv[])
{
    std::cout << boolalpha;
    vector<int> v{0, 1, 2, 3, 3, 4, 5, 5, 5, 6, 7, 8, 9};

    for (int i = 0; i < v.size(); i++)
    {
        cout << "v[" << i << "]=" << v[i] << " ";
    }
    cout << endl;

    int key = 5; // αν δεν δοθεί όρισμα γραμμής εντολών τότε χρησιμοποιείται ως κλειδί προς αναζήτηση η τιμή 5
    if (argc == 2)
        key = stoi(argv[1]);

    std::cout << "1) std::binary_search" << endl;
    std::cout << "Key = " << key << " found = " << binary_search(v.begin(), v.end(), key) << endl;

    std::cout << "2) std::lower_bound" << endl;
    auto itr1 = lower_bound(v.begin(), v.end(), key);
    if (itr1 == v.end())
        cout << "Lower bound for key = " << key << " not found" << endl;
    else
        cout << "Lower bound for key = " << key << " found at position " << itr1 - v.begin() << endl;

    std::cout << "3) std::upper_bound" << endl;
    auto itr2 = upper_bound(v.begin(), v.end(), key);
    if (itr2 == v.end())
        cout << "Upper bound for key = " << key << " not found" << endl;
    else
        cout << "Upper bound for key = " << key << " found at position " << itr2 - v.begin() << endl;

    for (auto it = itr1; it != itr2; it++)
    {
        cout << "a[" << (it - v.begin()) << "]=" << *it << endl;
    }

    cout << "4) std::equal_range" << endl;
    auto r = equal_range(v.begin(), v.end(), key);
    for (auto it = r.first; it != r.second; it++)
    {
        cout << "a[" << (it - v.begin()) << "]=" << *it << endl;
    }

    cout << "5) std::partition_point" << endl;
    auto pp = partition_point(v.begin(), v.end(), [&](auto const &e)
                              { return e < key; });
    for (auto it = pp; it != v.end() && *it == key; it++)
    {
        cout << "a[" << (it - v.begin()) << "]=" << *it << endl;
    }
}

/*
v[0]=0 v[1]=1 v[2]=2 v[3]=3 v[4]=3 v[5]=4 v[6]=5 v[7]=5 v[8]=5 v[9]=6 v[10]=7 v[11]=8 v[12]=9 
1) std::binary_search
Key = 5 found = true
2) std::lower_bound
Lower bound for key = 5 found at position 6
3) std::upper_bound
Upper bound for key = 5 found at position 9
a[6]=5
a[7]=5
a[8]=5
4) std::equal_range
a[6]=5
a[7]=5
a[8]=5
5) std::parition_point
a[6]=5
a[7]=5
a[8]=5
*/