import re 

A = input("Set A: ")
B = input("Set B: ")

A = set(re.findall(r"\d+",A))
B = set(re.findall(r"\d+",B))
A = set( [int(i) for i in A] )
B = set( [int(i) for i in B] )
def create_U(A, B):
    U = []
    for el in A:
        U.append(el)
    for el in B:
        if el not in A:
            U.append(el)
    return U

def return_bit(SET, U):
    SET_bit = ""
    for el in U:
        if el in SET:
            SET_bit += "1"
        else:
            SET_bit += "0"
    return SET_bit

def recreate(A_bit, U):
    res = set()
    for el in range(0, len(A_bit)):
        if A_bit[el] == "1":
            res.add(U[el])
    return res

def union(A, B, show = 1):
    U = create_U(A, B)
    A_bit = return_bit(A, U)
    B_bit = return_bit(B, U)
    res = ""
    for i, j in zip( list(A_bit), list(B_bit)):
        res += str( int(i) or int(j) )
    result = recreate(res, U)
    if show == 1:
        string = f"\n\t{A_bit}\nOR\n\t{B_bit}\n\t{'-'*len(A_bit)}\n\t{res}\n{result}\n"
        return string
    return result

def set_union(A, B):
    U = set()
    for el in A:
        U.add(el)
    for el in B:
        if el not in U:
            U.add(el)

    return U

def intersection(A, B, show = 1):
    U = create_U(A, B)
    A_bit = return_bit(A, U)
    B_bit = return_bit(B, U)
    res = ""
    for i, j in zip( list(A_bit), list(B_bit)):
        res += str( int(i) and int(j) )
    result = recreate(res, U)
    if len(result) == 0:
        return {}
    if show == 1:
        string = f"\n\t{A_bit}\nAND\n\t{B_bit}\n\t{'-'*len(A_bit)}\n\t{res}\n{result}\n"
        return string
    return result

def set_intersection(A, B):
    U = set()
    for el in A:
        U.add(el)
    for el in B:
        if el not in U:
            U.add(el)
    result = set()
    for el in U:
        if el in A and el in B:
            result.add(el)
    return result

def sym_difference(A, B, show = 1):
    U = create_U(A, B)
    A_bit = return_bit(A, U)
    B_bit = return_bit(B, U)
    res = ""
    for i, j in zip( list(A_bit), list(B_bit)):
        if int(i) != int(j):
            res += str( int(i) or int(j) )
        else:
            res += "0"
    result = recreate(res, U)
    if show == 1:
        string = f"\n\t{A_bit}\nXOR\n\t{B_bit}\n\t{'-'*len(A_bit)}\n\t{res}\n{result}\n"
        return string
    return result

def set_sym_difference(A, B):
    U = set()
    for el in A:
        U.add(el)
    for el in B:
        if el not in U:
            U.add(el)
    result = set()
    for el in U:
        if not (el in A and el in B):
            result.add(el)
    return result

def difference(A, B, show = 1):
    U = create_U(A, B)
    A_bit = return_bit(A, U)
    B_bit = return_bit(B, U)
    res = ""
    for i, j in zip( list(A_bit), list(B_bit)):
        if int(j) != 1:
            res += str( int(i) or int(j) )
        else:
            res += "0"
    result = recreate(res, U)
    if show == 1:
        string = f"\n\t{A_bit}\n--\n\t{B_bit}\n\t{'-'*len(A_bit)}\n\t{res}\n{result}\n"
        return string
    return result

def set_difference(A, B):
    result = set()
    for el in A:
        if el not in B:
            result.add(el)
    return result

def complement(A, U, show = 1):
    A_bit = return_bit(A, U)
    res = ""
    for i in list(A_bit):
        if i == "0":
            res += "1"
        else:
            res += "0"
    result = recreate(res, U)
    return result
    if show == 1:
        string = f"\n\t{A_bit}\nNOT\n\t{'-'*len(A_bit)}\n\t{res}\n{result}\n"
        return string

def set_complement(A, U):
    result = set()
    for el in U:
        if el not in A:
            result.add(el)
    return result

def product(A, B):
    prod = set()
    for el1 in A:
        for el2 in B:
            prod.add(tuple([el1, el2]))
    return prod

def is_equal(A, B):
    U = create_U(A, B)
    A_bit = return_bit(A, U)
    B_bit = return_bit(B, U)
    if A_bit == B_bit:
        return True
    else:
        return False

def is_subset(A, B):
    U = create_U(A, B)
    A_bit = return_bit(A, U)
    B_bit = return_bit(B, U)
    for a, b in zip( list(A_bit), list(B_bit) ):
        if a == "1" and b == "0":
            return False
    return True

UV = create_U(A, B)

print("\nВиконаємо операції без використання бітових рядків:\n")

print("Union: ", set_union(A, B))
print("Intersection: ", set_intersection(A, B))
print("Difference: ", set_difference(A, B))
print("Symmetric difference: ", set_sym_difference(A, B))
print("Complement for A: ", set_complement(A, UV))

print("\nВиконаємо операції, використовуючи бітове представлення множин: \n")

print("A in a bit string: ", return_bit(A, UV))
print("B in a bit string: ", return_bit(B, UV))
print("\nUnion: ", union(A, B))
print("Intersection: ", intersection(A, B))
print("Difference: ", difference(A, B))
print("Symmetric difference: ", sym_difference(A, B))
print("Complement for A: ", complement(A, UV))
print("Cartesian product: ", product(A, B)) 
print("Is A equals B? ", is_equal(A, B))
print("Is A a subset of B? ", is_subset(A, B))