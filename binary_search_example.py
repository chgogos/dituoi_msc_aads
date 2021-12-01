from bsearch_r import binary_search as binary_search_r
from bsearch_i import binary_search as binary_search_i


# δεδομένα εισόδου, ταξινομημένη ακολουθία
input_data = list(range(1, 100, 2))

# έλεγχος ότι τα αποτελέσματα από τις 2 υλοποιήσεις της δυαδικής αναζήτησης συμφωνούν
for key in input_data:
    pos1 = binary_search_i(input_data, key)
    pos2 = binary_search_r(input_data, key)
    print(f"key={key} {pos1} - {pos2}")
    assert pos1 == pos2

key = 101  # το κλειδί αυτό δεν υπάρχει στα δεδομένα εισόδου
pos1 = binary_search_i(input_data, key)
pos2 = binary_search_r(input_data, key)
print(f"key={key} {pos1} - {pos2}")
assert pos1 == pos2


# key=1 0 - 0
# key=3 1 - 1
# key=5 2 - 2
# key=7 3 - 3
# key=9 4 - 4
# key=11 5 - 5
# key=13 6 - 6
# key=15 7 - 7
# key=17 8 - 8
# key=19 9 - 9
# key=21 10 - 10
# key=23 11 - 11
# key=25 12 - 12
# key=27 13 - 13
# key=29 14 - 14
# key=31 15 - 15
# key=33 16 - 16
# key=35 17 - 17
# key=37 18 - 18
# key=39 19 - 19
# key=41 20 - 20
# key=43 21 - 21
# key=45 22 - 22
# key=47 23 - 23
# key=49 24 - 24
# key=51 25 - 25
# key=53 26 - 26
# key=55 27 - 27
# key=57 28 - 28
# key=59 29 - 29
# key=61 30 - 30
# key=63 31 - 31
# key=65 32 - 32
# key=67 33 - 33
# key=69 34 - 34
# key=71 35 - 35
# key=73 36 - 36
# key=75 37 - 37
# key=77 38 - 38
# key=79 39 - 39
# key=81 40 - 40
# key=83 41 - 41
# key=85 42 - 42
# key=87 43 - 43
# key=89 44 - 44
# key=91 45 - 45
# key=93 46 - 46
# key=95 47 - 47
# key=97 48 - 48
# key=99 49 - 49
# key=101 None - None
