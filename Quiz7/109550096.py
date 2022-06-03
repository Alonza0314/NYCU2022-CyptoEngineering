def algorithm(sequence):
    length=len(sequence)
    sequen=sequence[:]
    
    for i in range(length):
        if sequen[i]==1:
            break
    sett=set([i+1,0])
    j=i+1
    
    zero_set=set([0])
    temp_a=i
    temp_b=0
    
    for n in range(i+1,length):
        temp_d=0
        for element in sett:
            temp_d^=sequen[element+n-j]
        if temp_d==0:
            temp_b+=1
        else:
            if 2*j>n:
                sett^=set([temp_a-temp_b+element for element in zero_set])
                temp_b+=1
            else:
                temp_set=sett.copy()
                sett=set([temp_b-temp_a+element for element in sett])^zero_set
                j=n+j-1
                zero_set=temp_set
                temp_a,temp_b=temp_b,n-j+1
                
    def print_(polynomial):
        result=''
        listt=sorted(polynomial,reverse=True)
        for i in listt:
            if i==0:
                result+='1'
            else:
                result+='x^%s'%str(i)
            if i!=listt[-1]:
                result+=' + '
        return result
    
    return (print_(sett),j)

if __name__=='__main__':
    sequen=(0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 1, 1, 1, 0, 0, 1, 0, 0, 0, 1, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 0, 1, 0, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 0, 0, 1, 0, 1)
    (poly,span)=algorithm(sequen)
    
    print('Characteristic polynomial:(',poly,')')
    print('Linear span:(',span,')')