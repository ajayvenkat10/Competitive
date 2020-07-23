# t = int(input())
#
# for i in range(t):
#     n = int(input())
#     chefs = list(map(int,input().split()))
#     cheffetes = list(map(int,input().split()))
#     odd1 = []
#     odd2 = []
#     even1 = []
#     even2 = []
#
#     for i in range(n):
#         if(chefs[i] % 2 == 0):
#             even1.append(chefs[i])
#         else:
#             odd1.append(chefs[i])
#
#         if(cheffetes[i] % 2 == 0):
#             even2.append(cheffetes[i])
#         else:
#             odd2.append(cheffetes[i])
#
#     odd1.sort(reverse = True)
#     even1.sort(reverse = True)
#     odd2.sort(reverse = True)
#     even2.sort(reverse = True)
#
#     if(len(even1)<len(even2)):
#         size1 = len(even1)
#
#         even2 = even2[:len(even1)]
#     else:
#         size1 = len(even2)
#         even1 = even1[:size1]
#
#
#     # cheffetes1 = cheffetes
#     # chefs.sort()
#     # cheffetes1.sort()
#     # cheffetes.sort(reverse = True)
#     #
#     # sum1  = 0
#     # sum2 = 0
#     # for i in range(n):
#     #     sum1 += (chefs[i]+cheffetes[i])//2
#     #     sum2 += (chefs[i]+cheffetes1[i])//2
#
#     print(max(sum1,sum2))

t = int(input())

for i in range(t):
    n = int(input())
    chefs = list(map(int,input().split()))
    cheffetes = list(map(int,input().split()))
    even1 = 0
    odd1 = 0
    even2 = 0
    odd2 = 0

    for i in range(n):
        if(chefs[i] % 2 == 0):
            even1 += 1
        else:
            odd1 += 1

        if(cheffetes[i] % 2 == 0):
            even2 += 1
        else:
            odd2 += 1

    a = abs(odd1-odd2)
    b = abs(even1-even2)

    x = (a+b)//2

    ans = (sum(chefs) + sum(cheffetes) - x)//2

    print(ans)
