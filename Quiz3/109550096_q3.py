cin=list(input())
output=[]
for ind in range(len(cin)):
    if ind%5==0:
        num=ord(cin[ind])
        num-=(ord('C')-65)
        if num<65:
            num+=26
        output.append(chr(num))
    elif ind%5==1:
        num=ord(cin[ind])
        num-=(ord('R')-65)
        if num<65:
            num+=26
        output.append(chr(num))
    elif ind%5==2:
        num=ord(cin[ind])
        num-=(ord('Y')-65)
        if num<65:
            num+=26
        output.append(chr(num))
    elif ind%5==3:
        num=ord(cin[ind])
        num-=(ord('P')-65)
        if num<65:
            num+=26
        output.append(chr(num))
    else:
        num=ord(cin[ind])
        num-=(ord('T')-65)
        if num<65:
            num+=26
        output.append(chr(num))
for i in range(len(output)):
    print(output[i],end="")
