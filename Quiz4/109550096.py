from os import system
system('cls')

message='EOEYEGTRNPSECEHHETYHSNGNDDDDETOCRAERAEMHTECSEUSIARWKDRIRNYARANUEYICNTTCEIETUS'
example='WITHMALICETOWARDNONEWITHCHARITYFORALLWITHFIRMNESSINTHERIGHTASGODGIVESUSTOSEETHERIGHTLETUSSTRIVEONTOFINISHTHEWORKWEAREINTOBINDUPTHENATIONSWOUNDSTOCAREFORHIMWHOSHALLHAVEBORNETHEBATTLEANDFORHISWIDOWANDHISORPHANTODOALLWHICHMAYACHIEVEANDCHERISHAJUSTANDLASTINGPEACEAMONGOURSELVESANDWITHALLNATIONSGREECEANNOUNCEDYESTERDAYTHEAGRAGREEMENTWITHTRUKEYENDTHECYPRUSTHATTHEGREEKANDTURKISHCONTINGENTSWHICHARETOPARTICIPATEINTHETRIPARTITEHEADQUARTERSSHALLCOMPRISERESPECTIVELYGREEKOFFICERSNONCOMMISSIONEDOFFICERSANDMENANDTURKISHOFFICERSNONCOMMISSIONEDOFFICERSANDMENTHEPRESIDENTANDVICEPRESIDENTOFTHEREPUBLICOFCYPRUSACTINGINAGREEMENTMAYREQUESTTHEGREEKANDTURKISHGOVERNMENTSTOINCREASEORREDUCETHEGREEKANDTURKISHCONTINGENTSITISAGREEDTHATTHESITESOFTHECANTONMENTSFORTHEGREEKANDTURKISHCONTINGENTSPARTICIPATINGINTHETRIPARTITEHEADQUARTERSTHEIRJURIDICALSTATUSFACILITIESANDEXEMPTIONSINRESPECTOFCUSTOMSANDTAXESASWELLASOTHERIMMUNITIESANDPRIVILEGESANDANYOTHERMILITARYANDTECHNICALQUESTIONSCONCERNINGTHEORGANIZATIONANDOPERATIONOFTHEHEADQUARTERSMENTIONEDABOVESHALLBEDETERMINEDBYASPECIALCONVENTIONWHICHSHALLCOMEINTOFORCENOTLATERTHANTHETREATYOFALLIANCE'
arr=list(message)
arr_ex=list(example)

arr_7=[0]*7
arr_11=[0]*11

def check(character):
    if character=='A' or character=='E' or character=='I' or character=='O' or character=='U':
        return True
    else:
        return False
  
print('11x7:')
for i in range(77):
    if check(arr[i]):
        arr_7[i%7]+=1
for i in range(7):
    arr_7[i]/=11
print(arr_7)

print('7x11:')
for i in range(77):
    if check(arr[i]):
        arr_11[i%11]+=1
for i in range(11):
    arr_11[i]/=7
print(arr_11,'\n')

arr_dest=[[]for i in range(7)]

counting=0

for j in range(7):
    for i in range(11):
        arr_dest[j].append(arr[counting])
        counting+=1

for j in range(11):
    for i in range(7):
        print(arr_dest[i][j],end=' ')
    print()
print()

dict_dou=dict()
dict_tri=dict()

for i in range(len(arr_ex)-1):
    string=arr_ex[i]+arr_ex[i+1]
    if string in dict_dou:
        dict_dou[string]+=1
    else:
        dict_dou[string]=1
for i in range(len(arr_ex)-2):
    string=arr_ex[i]+arr_ex[i+1]+arr_ex[i+2]
    if string in dict_tri:
        dict_tri[string]+=1
    else:
        dict_tri[string]=1
for key,value in dict_tri.items():
    string=key[0]+key[1]
    dict_tri[key]=value/dict_dou[string]

def exchange_row(a,b):
    for i in range(11):
        temp=arr_dest[a][i]
        arr_dest[a][i]=arr_dest[b][i]
        arr_dest[b][i]=temp

exchange_row(0,2)
exchange_row(1,5)

print('GR')
for i in range(7):
    for j in range(11):
        print(arr_dest[i][j],end=' ')
    print()

counting=0
for j in range(11):
    string=arr_dest[0][j]+arr_dest[1][j]+arr_dest[2][j]
    if string in dict_tri:
        counting+=dict_tri[string]
print('\n2:',counting)
counting=0
for j in range(11):
    string=arr_dest[0][j]+arr_dest[1][j]+arr_dest[4][j]
    if string in dict_tri:
        counting+=dict_tri[string]
print('4:',counting)
counting=0
for j in range(11):
    string=arr_dest[0][j]+arr_dest[1][j]+arr_dest[5][j]
    if string in dict_tri:
        counting+=dict_tri[string]
print('5:',counting)

print('GRE')
for i in range(7):
    for j in range(11):
        print(arr_dest[i][j],end=' ')
    print()

counting=0
for j in range(11):
    string=arr_dest[1][j]+arr_dest[2][j]+arr_dest[3][j]
    if string in dict_tri:
        counting+=dict_tri[string]
print('\n3:',counting)
counting=0
for j in range(11):
    string=arr_dest[1][j]+arr_dest[2][j]+arr_dest[4][j]
    if string in dict_tri:
        counting+=dict_tri[string]
print('4:',counting)
counting=0
for j in range(11):
    string=arr_dest[1][j]+arr_dest[2][j]+arr_dest[5][j]
    if string in dict_tri:
        counting+=dict_tri[string]
print('5:',counting)
counting=0
for j in range(11):
    string=arr_dest[1][j]+arr_dest[2][j]+arr_dest[6][j]
    if string in dict_tri:
        counting+=dict_tri[string]
print('6:',counting)

exchange_row(3,4)
print('GREE')
for i in range(7):
    for j in range(11):
        print(arr_dest[i][j],end=' ')
    print()
    
counting=0
for j in range(11):
    string=arr_dest[2][j]+arr_dest[3][j]+arr_dest[4][j]
    if string in dict_tri:
        counting+=dict_tri[string]
print('\n4:',counting)
counting=0
for j in range(11):
    string=arr_dest[2][j]+arr_dest[3][j]+arr_dest[5][j]
    if string in dict_tri:
        counting+=dict_tri[string]
print('5:',counting)
counting=0
for j in range(11):
    string=arr_dest[2][j]+arr_dest[3][j]+arr_dest[6][j]
    if string in dict_tri:
        counting+=dict_tri[string]
print('6:',counting)

exchange_row(4,6)
print('GREEC')
for i in range(7):
    for j in range(11):
        print(arr_dest[i][j],end=' ')
    print()
    
counting=0
for j in range(11):
    string=arr_dest[3][j]+arr_dest[4][j]+arr_dest[5][j]
    if string in dict_tri:
        counting+=dict_tri[string]
print('\n5:',counting)
counting=0
for j in range(11):
    string=arr_dest[3][j]+arr_dest[4][j]+arr_dest[6][j]
    if string in dict_tri:
        counting+=dict_tri[string]
print('6:',counting)

print('GREECEA')
for i in range(7):
    for j in range(11):
        print(arr_dest[i][j],end=' ')
    print()

print('\nplaintext:')
for j in range(11):
    for i in range(7):
        print(arr_dest[i][j],end=' ')
    print()