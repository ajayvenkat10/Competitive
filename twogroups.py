# def two_groups(multiset):
#     sum1 = 0
#
#     for i in range(len(multiset)):
#         sum1 += multiset[i]
#
#     if sum1 % 2 != 0:
#         return False
#
#     divide = []
#
#     for i in range((sum1//2)+1):
#         divide.append([True] * (len(multiset)+1))
#
#     for i in range(len(multiset)+1):
#         divide[0][i] = True
#
#     for i in range(1, (sum1 // 2) + 1):
#         divide[i][0] = False
#
#     for i in range(1, (sum1 // 2) + 1):
#         for j in range(1, len(multiset)+ 1):
#             divide[i][j] = divide[i][j - 1]
#
#             if i >= multiset[j - 1]:
#                 divide[i][j] = (divide[i][j] or
#                               divide[i - multiset[j - 1]][j - 1])
#
#     return (divide[sum1 // 2][len(multiset)])
#
#
t = int(input())

for i in range(t):
    one,two,three = map(int, input().split())

    if((one%2 == 0 and two%2==0 and three%2==0)  or (one==two==three)):
        print("YES")

    else:
        if(one == 0):
            if(two and three):
                if((two + three) %2 == 0 and (two+three) != 2):
                    print("YES")

                else:
                    print("NO")

            else:
                if((two+three) % 2== 0):
                    print("YES")

                else:
                    print("NO")

        elif(three == 0):
            if(one and two):
                if((one + two)%2 == 0 and (one + two)!=2):
                    print("YES")

                else:
                    print("NO")

            else:
                if((two+three) % 2== 0):
                    print("YES")

                else:
                    print("NO")



        else:
            if((1*one + 3*three) %2 == 0):
                if(two > 0):
                    print("YES")

                else:
                    print("NO")

            else:
                print("NO")
