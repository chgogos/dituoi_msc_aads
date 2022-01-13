subsequences = set()

def all_subsequences(string, index, c):
    if index == len(string):
        if c != '':
            subsequences.add(c)
        return
    all_subsequences(string, index + 1, c + string[index])
    all_subsequences(string, index + 1, c)


all_subsequences("HELLO", 0, "")
print(sorted(subsequences))
