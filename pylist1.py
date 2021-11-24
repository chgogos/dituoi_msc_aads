import time

class PyList1:
    def __init__(self):
        self.items = []

    def append(self, item):
        self.items = self.items + [item]


class PyList2:
    def __init__(self):
        self.items = []

    def append(self, item):
        self.items.append(item)


if __name__ == "__main__":
    
    tic =  time.time()
    pl1 = PyList1()
    for i in range(100000):
        pl1.append(i)
    toc =  time.time()
    print(f'Time elapsed {toc - tic:2f}ms')
    
    tic =  time.time()
    pl2 = PyList2()
    for i in range(100000):
        pl2.append(i)
    toc =  time.time()
    print(f'Time elapsed {toc - tic:2f}ms')