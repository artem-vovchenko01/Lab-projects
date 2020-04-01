class Converter:
    def decimal_to_binary (self, num):
        if num > 1:
            return self.decimal_to_binary(num // 2) + str ( num % 2 )
        return str(num)

c = Converter()
num = 9
result = c.decimal_to_binary(num)
print(result)