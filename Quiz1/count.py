import collections

cin=input()

elements_count=collections.Counter(cin)

for key,value in elements_count.items():
    if key==' ':
        continue
    print(f"{key}:{value}")