def fun3(x):
    print(x)
    return x*2
    
def fun2(x):
    y = fun3(x)
    print(y)
    return y*2
    
def fun1(x):
    y = fun2(x)
    print(y)
    return y*2
    
fun1(42)

# 42
# 84
# 168