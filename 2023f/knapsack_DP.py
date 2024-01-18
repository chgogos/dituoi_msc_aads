from tabulate import tabulate


def knapsack_dp(v, w, C, n):
    V = [[0 for j in range(C + 1)] for i in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(C + 1):
            if w[i - 1] > j:
                V[i][j] = V[i - 1][j]
            else:
                V[i][j] = max(V[i - 1][j], V[i - 1][j - w[i - 1]] + v[i - 1])
    print(tabulate(V))
    print("Συνολική αξία σακιδίου = ", V[n][C])
    while n!=0:
        if V[n][C] != V[n-1][C]:
            print(f"Αντικείμενο = {n} Αξία = {v[n-1]} Βάρος = {w[n-1]}")
            C = C - w[n-1]
        n-=1


def example1():
    n = 4  # πλήθος αντικειμένων
    v = [3, 2, 4, 4]  # αξίες αντικειμένων
    w = [4, 3, 2, 3]  # βάρη αντικειμένων
    C = 6  # χωρητικότητα
    knapsack_dp(v, w, C, n)

def example2():
    v = [
        # fmt:off
        360, 83, 59, 130, 431, 67, 230, 52, 93, 125, 670, 892, 600, 38, 48, 147,
        78, 256, 63, 17, 120, 164, 432, 35, 92, 110, 22, 42, 50, 323, 514, 28,
        87, 73, 78, 15, 26, 78, 210, 36, 85, 189, 274, 43, 33, 10, 19, 389, 276,
        312
        #fmt:on
        ]  
    w = [
        #fmt:off
        7, 0, 30, 22, 80, 94, 11, 81, 70, 64, 59, 18, 0, 36, 3, 8, 15, 42, 9, 0,
        42, 47, 52, 32, 26, 48, 55, 6, 29, 84, 2, 4, 18, 56, 7, 29, 93, 44, 71,
        3, 86, 66, 31, 65, 0, 79, 20, 65, 52, 13
        #fmt:on
        ]  
    C = 850
    n = len(v)      

    knapsack_dp(v, w, C, n)

if __name__ == "__main__":
    example1()
    # example2()