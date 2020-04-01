number = 15


def to_binary(number):
    if number >= 1:
        return to_binary(number // 2) + str(number % 2)
    return ""


print(to_binary(number))
