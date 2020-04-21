#1.2.2.1
x = range(1, 11)
y = range(1, 10)

for col in x:
    for row in y:
        res = row*col
        if row == 9:
            print(row,"x",col,"=",res)
        else:
            if col == 10:
                print(row,"x",col,"=",res,end="      ")
            elif len(str(res)) == 2:
                print(row,"x",col,"=",res,end="       ")
            else:
                print(row,"x",col,"=",res,end="        ")


