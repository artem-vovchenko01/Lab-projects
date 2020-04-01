from Lab_package import *

T = MyBaseInit()
MyBaseAppendRecord(T,"Vovchenko","08.11.2001",17)
MyBaseAppendRecord(T, 'Ivanov','01.01.1972',30)
MyBaseAppendRecord(T, 'Sidorov','02.11.1969',33)
MyBaseAppendRecord(T, 'Petrov','23.30.1990',12)

MyBaseSave(T,"T.dat")
B = MyBaseRestore("T.dat")
print
print ('Тест First')
print (B)
MyBaseDeleteRecord(B,'Petrov')
print ('Тест Second')
print (B)


