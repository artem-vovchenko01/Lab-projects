import re
import unicodedata
func = "01110000"

print('Truth table: \n')
print(f"000\t| {func[0]} |\n001\t| {func[1]} |\n010\t| {func[2]} |\n011\t| {func[3]} |\n100\t| {func[4]} |\n101\t| {func[5]} |\n110\t| {func[6]} |\n111\t| {func[7]} |\n")

def save_0(func):
    if func[0] == "0":
        return True
    return False 

def save_1(func):
    if func[7] == "1":
        return True
    return False 

def make_dual(func):
    new_func = ""
    new_list = list(func)
    new_list.reverse()
    for el in new_list:
        if el == "0":
            new_func += "1"
        else: 
            new_func += "0"
    return new_func

def is_self_dual(func):
    if make_dual(func) == func:
        return True
    else:
        return False

def mod_2_sum(num1, num2):
    if (num1 == num2 == 1) or (num1 == num2 == 0):
        return 0
    else:
        return 1

def anf(func):
    col_1 = []
    for i in list(func):
        col_1.append(int(i))
    col_2 = []
    col_3 = []
    col_4 = []
    col_5 = []
    col_6 = []
    col_7 = []
    col_8 = []
    columns = {1 : col_1, 2 : col_2, 3 : col_3, 4 : col_4, 5 : col_5, 6 : col_6, 7 : col_7, 8 : col_8}
    for i in range(0,7):
        for j in range(0, 7-i):
            columns[i + 2].append( mod_2_sum( columns[i + 1][j], columns[i + 1][j + 1]))
    row = ""
    for i in range(1, 9):
        row += str(columns[i][0])
    variables = {0:1, 1:"Z", 2:"Y", 3:"YZ", 4:"X" ,5:"XZ", 6:"XY", 7:"XYZ"}
    final = ""
    for i in range(0, 8):
        if row[i] == "1":
            if i == 0:
                final += "1"
            else:
                if len(final) > 0:
                    final += f" \u2295 {variables[i]}"
                else:
                    final += f"{variables[i]}"
    return final

def is_linear(func):
    polynom = anf(func)
    matches = re.findall(r"\w\w+", func)
    if len(matches) >= 0:
        return False
    else:
        return True

def ddnf(func):
    function = {0:"000", 1:"001", 2:"010", 3:"011", 4:"100", 5:"101", 6:"110", 7:"111"}
    pos = {0:"X", 1:"Y", 2:"Z"}
    neg = {0: "¬X", 1:"¬Y", 2:"¬Z"}
    final = ""
    for i in range(0,8):
        if func[i] == "1":
            if len(final) > 0:
                final += " v "
            for j in range(0, 3):
                if function[i][j] == "1":
                    final += pos[j]
                else:
                    final += neg[j]
    return final

def dknf(func):
    function = {0:"000", 1:"001", 2:"010", 3:"011", 4:"100", 5:"101", 6:"110", 7:"111"}
    pos = {0:"X", 1:"Y", 2:"Z"}
    neg = {0: "¬X", 1:"¬Y", 2:"¬Z"}
    final = ""
    for i in range(0,8):
        if func[i] == "0":
            if len(final) > 0:
                final += ") ∧ ("
            else:
                final += "("
            for j in range(0, 3):
                if function[i][j] == "0":
                    final += pos[j]
                else:
                    final += neg[j]
                if j != 2:
                    final += " v "
    final += ")"
    return final

print("Saves 0?") 
print(save_0(func), "\n")
print("Saves 1?")
print(save_1(func), "\n")   
print("Dual?: ")
print(make_dual(func), "\n")
print("Self dual?")
print(is_self_dual(func), "\n")
print("Linear?")
print(is_linear(func), "\n")
print("ANF: ")
print(anf(func), "\n")
print("Perfect DNF: ")
print(ddnf(func), "\n")
print("Perfect CNF: ")
print(dknf(func), "\n")
