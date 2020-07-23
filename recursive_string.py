from collections import defaultdict
n = int(input())
incomplete = list(map(int,input().split()))

m = int(input())
original = list(map(int,input().split()))

dict_ori = defaultdict(int)
dict_inc = defaultdict(int)

for i in range(m):
    dict_ori[original[i]] += 1

for i in range(n):
    dict_inc[incomplete[i]] += 1

answer = []
ori_set = list(set(original))

for i in range(len(ori_set)):
    if(dict_inc[ori_set[i]] < dict_ori[ori_set[i]]):
        answer.append(ori_set[i])

answer.sort()
print(* answer)
