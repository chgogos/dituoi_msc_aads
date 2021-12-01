import time

class PyList:
    def __init__(self, size=1):
        self.items = [None] * size
        self.numItems = 0

    def append(self, item):
        if self.numItems == len(self.items):
            # newlst = [None] * (len(self.items) + 1) # σενάριο α) οδηγεί σε amortized χρόνο O(n)
            newlst = [None] * len(self.items) * 2   # σενάριο β) οδηγεί σε amortized χρόνο O(1) (οτιδήποτε είναι αναλογικό του μεγέθους της λίστας)
            for k in range(len(self.items)):
                newlst[k] = self.items[k]
            self.items = newlst
        self.items[self.numItems] = item
        self.numItems += 1


if __name__ == "__main__":
    
    tic =  time.time()
    pl = PyList()
    for i in range(10000):
        pl.append(i)
    toc =  time.time()
    print(f'{pl.numItems}/{len(pl.items)}')
    print(f'Χρόνος που πέρασε {toc - tic:2f}ms')
    

# σενάριο α) οδηγεί σε amortized χρόνο O(n)
# 10000/10000
# Χρόνος που πέρασε 4.145984ms

# σενάριο β) οδηγεί σε amortized χρόνο O(1)
# 10000/16384
# Χρόνος που πέρασε 0.003973ms


