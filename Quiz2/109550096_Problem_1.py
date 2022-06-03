'''
ECDTMECAERAUOOLEDSAMMERNENASSODYTNRVBNLCRLTIQLAETRIGAWEBAAEIHOR
'''

import numpy as np

line=input()
arr=list(line)

temp_arr1=[[]for i in range(9)]
temp_arr2=[[]for i in range(7)]

def check(character):
    if character=='A' or character=='E' or character=='I' or character=='O' or character=='U':
        return True
    else:
        return False

for i in range(0,9):
    for j in range(0,7):
        temp_arr1[i].append(arr[i*7+j])

final1=0
for j in range(0,7):
    counting=0
    for i in range(0,9):
        print(temp_arr1[i][j],end=" ")
        if check(temp_arr1[i][j]):
            counting+=1
    print(abs(counting-0.4*9))
    final1+=abs(counting-0.4*9)
print(final1)
print()

for i in range(0,7):
    for j in range(0,9):
        temp_arr2[i].append(arr[i*9+j])

final2=0
for j in range(0,9):
    counting=0
    for i in range(0,7):
        print(temp_arr2[i][j],end=" ")
        if check(temp_arr2[i][j]):
            counting+=1
    print(abs(counting-0.4*7))
    final2+=abs(counting-0.4*7)
print(final2)