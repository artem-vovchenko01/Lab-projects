arr = [1, 2, 3, 4, 5]


def arr_sum(arr, pos=-1, result=0):
    if pos != len(arr) - 1:
        pos += 1
        result += arr_sum(arr, pos, result)
        return result + arr[pos]
    return 0


print(arr_sum(arr))
