import math
def fact (n):
    """ Factorial """
    result = 1
    for i in range(1,n+1):
        result *=i
    return result

def log_fact (n):
    """ log(n!) """
    return math.log(fact(n), 2)

def nlogn (n):
    """ nlogn """
    return n * math.log(n, 2)

def compare (num):
    """ Compares O(log(N!)) with O(nlog(n)). With each iteraton prints log(n!) / (nlog(n) - n) """
    for i in range(3, num):
        print(f"Num: {i} ", log_fact(i) / (nlogn(i) - i))

num = 2000
compare(num)