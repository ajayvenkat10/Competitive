from collections import defaultdict

name1 = input()
name2 = input()
final = input()

dict_n = defaultdict(int)
dict_f = defaultdict(int)

for i in name1:
    dict_n[i] += 1

for i in name2:
    dict_n[i] += 1

for i in final:
    dict_f[i] += 1

if(dict_f == dict_n):
    print("YES")

else:
    print("NO")

