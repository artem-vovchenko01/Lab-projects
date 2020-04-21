# code author : Muravinets Misha
class task5:
    __nums = [str(i) for i in range(10)]
    __operations = ["+", "-", "*", "/"]

    def __init__(self, priklad):
        self.pr = priklad

    def calculate(self):
        if self.pr[0] not in self.__nums:
            raise Exception("Nummbers should only be within the 0-9 range")
        self.__sum = int(self.pr[0])
        for i in range(1, len(self.pr), 2):
            if self.pr[i + 1] not in self.__nums:
                raise Exception("Nummbers should only be within the 0-9 range")
            if self.pr[i] not in self.__operations:
                raise Exception("Operations can only be '*','/','+','-'")
            if self.pr[i] == "+":
                self.__sum = self.__sum + int(self.pr[i + 1])
            elif self.pr[i] == "-":
                self.__sum = self.__sum - int(self.pr[i + 1])
            elif self.pr[i] == "*":
                self.__sum = self.__sum * int(self.pr[i + 1])
            elif self.pr[i] == "/":
                self.__sum = self.__sum / int(self.pr[i + 1])

    def result(self):
        print(self.__sum)


test = task5("2+3-1*5/2")
test.calculate()
test.result()
