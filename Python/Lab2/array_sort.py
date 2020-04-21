import array, random
# Creating an empty array.
arr = array.array("i", [])

# Filling the array with random integers.
for i in range(1, 101):
    arr.append( random.randint(1,1000) )

def asc(arr_sort):
    """
This function sorts the input array in ascending.
    """
    return sorted(arr_sort)

def desc(arr_sort):
    """
This function sorts the input array in descending.
    """
    return sorted(arr_sort, reverse=True)

print("Вдсортовано за зростанням: ",asc(arr))
print("Відсортовано за спаданням: ",desc(arr))