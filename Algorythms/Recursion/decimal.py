number = 488494448888888888888888888888888888888835908630924095724938603406535932476093427057809632960834259734206475973420958345908888999999999999999999999500000083498350976349863957058092347630988


def print_decimals(number):
    if number > 1:
        print_decimals(number / 10)
        print(number)


print_decimals(number)