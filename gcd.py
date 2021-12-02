def gcd(x,y):
    print(f'x={x}, y={y}')
    if y == 0:
        return x
    return gcd(y, x % y)

print(gcd(3220,2245))