with open("sample_text.txt") as f:
    text = f.read()

braces = ""
while True:
    index_open = None
    index_close = None
    for i in range(0,len(text)):
        char = text[i]
        if char == "(":
            index_open = i
    if index_open == None:
        for i in range(0,len(text)):
            char = text[i]
            if char == ")":
                print("Дужки розставлено неправильно")
                quit()
    if index_open == None:
        print("Дужки розставлено правильно")
        quit()
                    
    for i in range(index_open,len(text)):
        char = text[i]
        if char == ")":
            index_close = i
            break
    if index_open == None and index_close == None:
        print("Дужки розставлено правильно")
        quit()
    if index_open == None or index_close == None:
        print("Дужки розставлено неправильно")
        quit()
    if index_open < index_close:
        text = text[:index_open] + text[index_open+1:index_close] + text[index_close+1:]
    else: print("Дужки розставлено неправильно")
