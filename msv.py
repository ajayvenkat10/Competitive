# import math
#
# def find_factors(num) :
#     factors_array = []
#     square_root = int(math.sqrt(num))
#     for i in range(1,square_root+1):
#         if (num % i == 0) :
#             if (num // i == i) :
#                 factors_array.append(i)
#
#             else :
#                 factors_array.append(i)
#                 factors_array.append(num//i)
#
#     return factors_array
#
# from collections import defaultdict
#
# t = int(input())
#
# while(t):
#     t-=1
#     n = int(input())
#     sequence = list(map(int, input().split()))
#     last_index = [0]*10000000
#     visited = [0]*10000000
#
#     for i in range(len(sequence)):
#         last_index[sequence[i]] = i
#         visited[sequence[i]] += 1
#
#     counter = defaultdict(int)
#
#     for i in range(n-1):
#         fact = find_factors(sequence[i])
#         for j in range(len(fact)):
#             if(visited[fact[j]]):
#                 if(last_index[fact[j]] > i):
#                     counter[fact[j]] += 1
#                 else:
#                     counter[fact[j]] = counter[fact[j]]
#
#     valid_numbers = counter.keys()
#     valid_numbers = list(valid_numbers)
#
#     for i in range(len(valid_numbers)):
#         vis = visited[valid_numbers[i]]
#         minimum = min(0,vis-1)
#         counter[valid_numbers[i]] += minimum
#
#     if not counter:
#         maximum_star_value = 0
#
#     else:
#         star_values = counter.values()
#         star_values = list(star_values)
#         maximum_star_value = max(star_values)
#
#     print(maximum_star_value)
t=int(input())
for i in range(0,t):
    n=int(input())
    a=[int(i) for i in input().split()]
    count=0
    start=0
    for i in range(1,n):
        if i <= 5:
            start=0
        if(i==1 and a[i] < min(a[start:i])):
            count+=1
        elif(i==2 and a[i] < min(a[start:i])):
            count+=1
        elif(i==3 and a[i] < min(a[start:i])):
            count+=1
        elif(i==4 and a[i] < min(a[start:i])):
            count+=1
        elif(i==5 and a[i] < min(a[start:i])):
            count+=1
        elif(i>5 and a[i] < min(a[i-5:i])):
            count+=1
    print(count+1)
