import bisect


def find_index(elements, value):
    """επιστρέφει το δείκτη της πρώτης θέσης από αριστερά στην οποία βρίσκεται η τιμή value, ή None αν δεν υπάρχει"""
    index = bisect.bisect_left(
        elements, value
    )  # επιστρέφει τη θέση στην οποία στην οποία θα πρέπει να εισαχθεί το value για να εξακολουθεί η λίστα να είναι ταξινομημένη
    if index < len(elements) and elements[index] == value:
        return index


a_list = [1, 2, 4, 5, 6, 9, 11, 20]

a_key = 5
print(find_index(a_list, a_key))
a_key = 7
print(find_index(a_list, a_key))

# 3
# None
