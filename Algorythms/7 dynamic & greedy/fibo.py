def fibo_exp (n):
    if n <= 1:
        return 1
    return fibo_exp(n-1) + fibo_exp(n-2)

def fibo_bottom_up (n):
    arr = [1 for i in range(0,n+1)]
    for i in range(2, n+1):
        arr[i] = arr[i-1] + arr[i-2]
    return arr[n]

def fibo_top_down(n):
    lookup = [None] * (n+1)
    lookup[0] = 1
    lookup[1] = 1
    def fibo (k):
        if lookup[k] is None:
            lookup[k] = fibo(k-1) + fibo(k-2)
        return lookup[k]
    return fibo(n)

print(fibo_top_down(20))
print(fibo_bottom_up(20))
print(fibo_exp(20))

# f 2 = 2
# f 3 = f2 + f1 = 3
# f 4 = f3 + f2 = 5
# f 5  = f4 + f3 = 8