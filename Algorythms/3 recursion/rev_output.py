txt = input("Provide a string with 0 at the end: ")
nums = [int(x) for x in txt.split()]


def print_reversed(arr, pos=0):
    num = arr[pos]
    pos += 1
    if num != 0:
        print_reversed(arr, pos)
    print(num, end=" ")


def print_reversed_non_recursion(arr):
    pos = -1
    length = len(arr)
    for i in range(length):
        print(arr[pos], end=" ")
        pos = pos - 1


print_reversed(nums)
print()
print_reversed_non_recursion(nums)
