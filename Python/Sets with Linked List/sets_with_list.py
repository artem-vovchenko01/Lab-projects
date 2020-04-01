import re 
from  doubly_linked_list import Node
from doubly_linked_list import DoublyLinkedList
from doubly_linked_list import DoublyLinkedListTester as tester

rawA = input("Set A: ")
rawB = input("Set B: ")

inpA = re.findall(r"\d+",rawA)
inpB = re.findall(r"\d+",rawB)
try:
    temp = [int(i) for i in inpA]
    temp = [int(i) for i in inpB]
except:
    print("Please provide space separated lists of integers. ")
    quit()
A = DoublyLinkedList()
B = DoublyLinkedList()
for el in inpA:
    val = int(el)
    if not A.search(val):
        A.add(val)
for el in inpB:
    val = int(el)
    if not B.search(val):
        B.add(val)

def create_U(A, B) -> DoublyLinkedList:
    """ Returns union of 2 iterables """
    U = DoublyLinkedList()
    for el in A:
        U.add(el)
    for el in B:
        if el not in A:
            U.add(el)
    return U

def return_bit(SET, U) -> str:
    """ Returns bit representation of SET according to universal set U """
    SET_bit = ""
    for el in U:
        if el in SET:
            SET_bit += "1"
        else:
            SET_bit += "0"
    return SET_bit

def recreate(A_bit, U) -> DoublyLinkedList:
    """ Creates DoublyLinkedList from U considering A_bit bit representation """
    res = DoublyLinkedList()
    for el in range(0, len(A_bit)):
        if A_bit[el] == "1":
            res.add(U[el])
    return res

def union(A, B) -> str:
    """ Returns bit representation of union of two iterables """
    U = create_U(A, B)
    A_bit = return_bit(A, U)
    B_bit = return_bit(B, U)
    res = ""
    for i, j in zip( DoublyLinkedList(A_bit), DoublyLinkedList(B_bit) ):
        res += str( int(i) or int(j) )
    result = recreate(res, U)
    string = f"\n\t{A_bit}\nOR\n\t{B_bit}\n\t{'-'*len(A_bit)}\n\t{res}\n{result}\n"
    return string

def set_union(A, B) -> DoublyLinkedList:
    """ Returns union of A and B """
    U = DoublyLinkedList()
    for el in A:
        U.add(el)
    for el in B:
        if el not in U:
            U.add(el)
    return U

def intersection(A, B) -> str:
    """ Returns bit representation of intersectin"""
    U = create_U(A, B)
    A_bit = return_bit(A, U)
    B_bit = return_bit(B, U)
    res = ""
    for i, j in zip( DoublyLinkedList(A_bit), DoublyLinkedList(B_bit) ):
        res += str( int(i) and int(j) )
    result = recreate(res, U)
    string = f"\n\t{A_bit}\nAND\n\t{B_bit}\n\t{'-'*len(A_bit)}\n\t{res}\n{result}\n"
    return string

def set_intersection(A, B) -> DoublyLinkedList:
    """ Returns intersection of A and B """
    U = DoublyLinkedList()
    for el in A:
        U.add(el)
    for el in B:
        if el not in U:
            U.add(el)
    result = DoublyLinkedList()
    for el in U:
        if el in A and el in B:
            result.add(el)
    return result

def sym_difference(A, B) -> str:
    """ Returns bit representation of symmetric difference """
    U = create_U(A, B)
    A_bit = return_bit(A, U)
    B_bit = return_bit(B, U)
    res = ""
    for i, j in zip( DoublyLinkedList(A_bit), DoublyLinkedList(B_bit) ):
        if int(i) != int(j):
            res += str( int(i) or int(j) )
        else:
            res += "0"
    result = recreate(res, U)
    string = f"\n\t{A_bit}\nXOR\n\t{B_bit}\n\t{'-'*len(A_bit)}\n\t{res}\n{result}\n"
    return string

def set_sym_difference(A, B) -> DoublyLinkedList:
    U = DoublyLinkedList( set_union(A, B) )
    result = DoublyLinkedList()
    for el in U:
        if not (el in A and el in B):
            result.add(el)
    return result

def difference(A, B) -> str:
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
    string = f"\n\t{A_bit}\n--\n\t{B_bit}\n\t{'-'*len(A_bit)}\n\t{res}\n{result}\n"
    return string

def set_difference(A, B) -> DoublyLinkedList:
    """ Returns A \ B (set difference) """
    result = DoublyLinkedList()
    for el in A:
        if el not in B:
            result.add(el)
    return result

def complement(A, U) -> str:
    A_bit = return_bit(A, U)
    res = ""
    for i in list(A_bit):
        if i == "0":
            res += "1"
        else:
            res += "0"
    result = recreate(res, U)
    string = f"\n\t{A_bit}\nNOT\n\t{'-'*len(A_bit)}\n\t{res}\n{result}\n"
    return string

def set_complement(A, U) -> DoublyLinkedList:
    """ Returns complement of A considering U as universal set """
    result = DoublyLinkedList()
    for el in U:
        if el not in A:
            result.add(el)
    return result

def product(A, B) -> DoublyLinkedList:
    """ Returns list of tuples with all Cartesian product's pairs """
    prod = DoublyLinkedList()
    for el1 in A:
        for el2 in B:
            prod.add(  (el1, el2)  )
    return prod

def is_equal(A, B) -> bool:
    """ Returns true if A and B are equal as sets, else False """
    U = create_U(A, B)
    A_bit = return_bit(A, U)
    B_bit = return_bit(B, U)
    if A_bit == B_bit:
        return True
    else:
        return False

def is_subset(A, B) -> bool:
    """ Returns true if A is a subset of B, else False """
    U = create_U(A, B)
    A_bit = return_bit(A, U)
    B_bit = return_bit(B, U)
    for a, b in zip( DoublyLinkedList(A_bit), DoublyLinkedList(B_bit) ):
        if a == "1" and b == "0":
            return False
    return True

UV = create_U(A, B)

print("\nCompleted operations without using bit strings:\n")
print(f"A: ", A)
print(f"B: ", B)
print("Union: ", set_union(A, B))
print("Intersection: ", set_intersection(A, B))
print("Difference (A \ B): ", set_difference(A, B))
print("Difference (B \ A): ", set_difference(B, A))
print("Symmetric difference: ", set_sym_difference(A, B))
print("Complement for A: ", set_complement(A, UV))
print("Complement for B: ", set_complement(B, UV))

print("\nCompleted operations using bit set representation: \n")

print("A in a bit string: ", return_bit(A, UV))
print("B in a bit string: ", return_bit(B, UV))
print("\nUnion: ", union(A, B))
print("Intersection: ", intersection(A, B))
print("Difference (A \ B): ", difference(A, B))
print("Difference (B \ A): ", difference(B, A))
print("Symmetric difference: ", sym_difference(A, B))
print("Complement for A: ", complement(A, UV))
print("Complement for B: ", complement(B, UV))
print("Cartesian product: ", product(A, B)) 
print("Is A equals B? ", is_equal(A, B))
print("Is A a subset of B? ", is_subset(A, B))
print("Is B a subset of A? ", is_subset(B, A))
