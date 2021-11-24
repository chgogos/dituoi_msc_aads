import time

class PyList:
    def __init__(self, size=1):
        self.items = [None] * size
        self.numItems = 0

    def append(self, item):
        if self.numItems == len(self.items):
            newlst = [None] * len(self.items) * 2   # οδηγεί σε amortized χρόνο O(1) (οτιδήποτε είναι αναλογικό του μεγέθους της λίστας)
            # newlst = [None] * (len(self.items) + 1) # οδηγεί σε amortized χρόνο O(n)
            for k in range(len(self.items)):
                newlst[k] = self.items[k]
            self.items = newlst
        self.items[self.numItems] = item
        self.numItems += 1


if __name__ == "__main__":
    
    tic =  time.time()
    pl = PyList()
    for i in range(100000):
        pl.append(i)
    toc =  time.time()
    print(f'{pl.numItems}/{len(pl.items)}')
    print(f'Χρόνος που πέρασε {toc - tic:2f}ms')
    
