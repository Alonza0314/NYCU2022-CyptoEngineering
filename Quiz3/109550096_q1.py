'''message1 Len=5
Len = 4 :  0.04091422889361049
Len = 5 :  0.06575767270709668
Len = 6 :  0.0409509053353688
Len = 7 :  0.04166062944082544
'''
'''message2 Len=5
Len = 4 :  0.043477589719814025
Len = 5 :  0.06575767270709668
Len = 6 :  0.04327527712025824
Len = 7 :  0.04369997366111141
'''
'''message3 Len=6
Len = 4 :  0.04471388881468223
Len = 5 :  0.04133164277800678
Len = 6 :  0.07013502242860041
Len = 7 :  0.04247888079842709
'''

from collections import Counter as ct

file=open('message1.txt')
cin=file.readline()
line=list(cin)

#4
a=[]
b=[]
c=[]
d=[]
for ind in range(len(line)):
    if ind%4==0:
        a.append(line[ind])
    elif ind%4==1:
        b.append(line[ind])
    elif ind%4==2:
        c.append(line[ind])
    else:
        d.append(line[ind])

count_a=ct(a)
count_b=ct(b)
count_c=ct(c)
count_d=ct(d)

N_a=0
F_a=0
for key,value in count_a.items():
    N_a+=value
    F_a+=(value*(value-1))
    
N_b=0
F_b=0
for key,value in count_b.items():
    N_b+=value
    F_b+=(value*(value-1))
    
N_c=0
F_c=0
for key,value in count_c.items():
    N_c+=value
    F_c+=(value*(value-1))

N_d=0
F_d=0
for key,value in count_d.items():
    N_d+=value
    F_d+=(value*(value-1))
    
output=(F_a/(N_a*(N_a-1)))+(F_b/(N_b*(N_b-1)))+(F_c/(N_c*(N_c-1)))+(F_d/(N_d*(N_d-1)))

final=4
temp=abs(0.068-output/4)

#5
e=[]
f=[]
g=[]
h=[]
i=[]
for ind in range(len(line)):
    if ind%5==0:
        e.append(line[ind])
    elif ind%5==1:
        f.append(line[ind])
    elif ind%5==2:
        g.append(line[ind])
    elif ind%5==3:
        h.append(line[ind])
    else:
        i.append(line[ind])

count_e=ct(e)
count_f=ct(f)
count_g=ct(g)
count_h=ct(h)
count_i=ct(i)

N_e=0
F_e=0
for key,value in count_e.items():
    N_e+=value
    F_e+=(value*(value-1))
N_f=0
F_f=0
for key,value in count_f.items():
    N_f+=value
    F_f+=(value*(value-1))
N_g=0
F_g=0
for key,value in count_g.items():
    N_g+=value
    F_g+=(value*(value-1))
N_h=0
F_h=0
for key,value in count_h.items():
    N_h+=value
    F_h+=(value*(value-1))
N_i=0
F_i=0
for key,value in count_i.items():
    N_i+=value
    F_i+=(value*(value-1))

output=(F_e/(N_e*(N_e-1)))+(F_f/(N_f*(N_f-1)))+(F_g/(N_g*(N_g-1)))+(F_h/(N_h*(N_h-1)))+(F_i/(N_i*(N_i-1)))

if temp>abs(0.068-output/5):
    final=5
    temp=abs(0.068-output/5)

#6
j=[]
k=[]
l=[]
m=[]
n=[]
o=[]
for ind in range(len(line)):
    if ind%6==0:
        j.append(line[ind])
    elif ind%6==1:
        k.append(line[ind])
    elif ind%6==2:
        l.append(line[ind])
    elif ind%6==3:
        m.append(line[ind])
    elif ind%6==4:
        n.append(line[ind])
    else:
        o.append(line[ind])

count_j=ct(j)
count_k=ct(k)
count_l=ct(l)
count_m=ct(m)
count_n=ct(n)
count_o=ct(o)

N_j=0
F_j=0
for key,value in count_j.items():
    N_j+=value
    F_j+=(value*(value-1))
N_k=0
F_k=0
for key,value in count_k.items():
    N_k+=value
    F_k+=(value*(value-1))
N_l=0
F_l=0
for key,value in count_l.items():
    N_l+=value
    F_l+=(value*(value-1))
N_m=0
F_m=0
for key,value in count_m.items():
    N_m+=value
    F_m+=(value*(value-1))
N_n=0
F_n=0
for key,value in count_n.items():
    N_n+=value
    F_n+=(value*(value-1))
N_o=0
F_o=0
for key,value in count_o.items():
    N_o+=value
    F_o+=(value*(value-1))

output=(F_j/(N_j*(N_j-1)))+(F_k/(N_k*(N_k-1)))+(F_l/(N_l*(N_l-1)))+(F_m/(N_m*(N_m-1)))+(F_n/(N_n*(N_n-1)))+(F_o/(N_o*(N_o-1)))

if temp>abs(0.068-output/6):
    final=6
    temp=abs(0.068-output/6)

#7
p=[]
q=[]
r=[]
s=[]
t=[]
u=[]
v=[]
for ind in range(len(line)):
    if ind%7==0:
        p.append(line[ind])
    elif ind%7==1:
        q.append(line[ind])
    elif ind%7==2:
        r.append(line[ind])
    elif ind%7==3:
        s.append(line[ind])
    elif ind%7==4:
        t.append(line[ind])
    elif ind%7==5:
        u.append(line[ind])
    else:
        v.append(line[ind])

count_p=ct(p)
count_q=ct(q)
count_r=ct(r)
count_s=ct(s)
count_t=ct(t)
count_u=ct(u)
count_v=ct(v)

N_p=0
F_p=0
for key,value in count_p.items():
    N_p+=value
    F_p+=(value*(value-1))
N_q=0
F_q=0
for key,value in count_q.items():
    N_q+=value
    F_q+=(value*(value-1))
N_r=0
F_r=0
for key,value in count_r.items():
    N_r+=value
    F_r+=(value*(value-1))
N_s=0
F_s=0
for key,value in count_s.items():
    N_s+=value
    F_s+=(value*(value-1))
N_t=0
F_t=0
for key,value in count_t.items():
    N_t+=value
    F_t+=(value*(value-1))
N_u=0
F_u=0
for key,value in count_u.items():
    N_u+=value
    F_u+=(value*(value-1))
N_v=0
F_v=0
for key,value in count_v.items():
    N_v+=value
    F_v+=(value*(value-1))
    
output=(F_p/(N_p*(N_p-1)))+(F_q/(N_q*(N_q-1)))+(F_r/(N_r*(N_r-1)))+(F_s/(N_s*(N_s-1)))+(F_t/(N_t*(N_t-1)))+(F_u/(N_u*(N_u-1)))+(F_v/(N_v*(N_v-1)))
if temp>abs(0.068-output/7):
    final=7
    temp=abs(0.068-output/7)
    
print(final)

file.close()