class Converter:
    def decimal_to_binary (self, num):
        result = ""
        while num > 1:
            result = str(num % 2) + result
            num //= 2
        return str(num) + result
        
c = Converter()
num = 9
print(c.decimal_to_binary(num))