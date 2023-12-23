def square_root(n, epsilon = 0.0000001):
    if n < 0:
        raise ValueError("n must be non-negative")
    if n < 1:
        low = n
        high = 1
    else:
        low = 0
        high = n
    while low < high:
        middle = (low + high) / 2
        if abs(middle * middle - n) < epsilon:
            return middle
        if middle * middle > n:
            high = middle
        else:
            low = middle
    
if __name__ == "__main__":
    x = square_root(400)
    print(x)