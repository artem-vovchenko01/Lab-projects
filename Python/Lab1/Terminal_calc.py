num=input('Type your desired number: ')
try:
        num=int(num)
except:
    try:
        num=float(num)
    except:
        print('Your number is incorrect. Try again.')
        quit()

factor=input('Choose what to do: 1: *, 2: /, 3: +, 4: -, 5: ** ')
    
if factor=='1':
    factor='*'
elif factor=='2':
    factor='/'
elif factor=='3':
    factor='+'
elif factor=='4':
    factor='-'
elif factor=='5':
    factor='**'
else: 
    print('Your sign is incorrect. Try again')
    quit()

factor_num=input('Type argument: ')

try:
    try:
        factor_num=int(factor_num)
    except:
        factor_num=float(factor_num)
except:
    print('Oh, please, type real number!')
    quit()

text="Your result is: "

if factor=='*':
    res=num*factor_num
elif factor=='/':
    res=num/factor_num
elif factor=='+':
    res=num+factor_num
elif factor=='-':
    res=num - factor_num
elif factor=='**':
    res=num**factor_num

print(text, res)