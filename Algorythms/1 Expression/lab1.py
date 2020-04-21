class ParseCalc:
    def calculate(self):
        text = input("Enter the expression: ")
        init = int(text[0])
        for pos in range(1, len(text), 2):
            if not(text[pos-1].isdigit() and text[pos+1].isdigit() and text[pos] in ["*","/","+","-"]):
                raise Exception("Illegal argument")
            if text[pos] == "*":
                init *= int(text[pos+1])
            elif text[pos] == "/":
                init /= int(text[pos+1])
            elif text[pos] == "+":
                init += int(text[pos+1])
            elif text[pos] == "-":
                init -= int(text[pos+1])
        return init
print(ParseCalc.calculate(ParseCalc()))