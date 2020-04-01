number = 1000


def get_nums(number):
    if number >= 1:
        return get_nums(number // 10) + 1
    return 0


print(get_nums(number))
