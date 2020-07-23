# t  = int(input())
#
# for i in range(t):
#     l, r = map(int, input().split())
#
#     binary  = bin(r)
#     binary = list(binary[2:])
#
#     ans = r
#     for i in range(len(binary)):
#         if(binary[i] == '0'):
#             num = int('1'* (len(binary)-i),2)
#
#             if(num>=l):
#                 ans =  r | num
#                 break
#
#             else:
#                 alter = bin(l)
#                 alter = list(alter[2:])
#
#                 for j in range(len(alter)-1,-1,-1):
#                     if(alter[j] == '0'):
#                         alter[j] = '1'
#                         if(alter>=binary):
#                             alter[j] = '0'
#                             break
#
#                 alter = int(''.join(alter),2)
#                 ans = r | alter
#                 break
#
#     print(ans)

t  = int(input())

for i in range(t):
    l, r = map(int, input().split())

    binary  = bin(r)
    binary = binary[2:]
    binary = list(binary)

    ans = r
    for i in range(len(binary)):
        if(binary[i] == '0'):
            num = ['1'] * (len(binary)-i)
            num = int(''.join(num),2)

            if(num < r and num>=l):
                ans =  r | num
                break

            else:
                alter = bin(l)
                alter = alter[2:]
                alter = list(alter)

                for j in range(len(alter)-1,-1,-1):
                    if(alter[j] == '0'):
                        x = alter[:]
                        x[j] == '1'
                        x = int(''.join(x),2)

                        if(x>=r):
                            break

                        else:
                            alter[j] = '1'

                alter = ''.join(alter)
                alter = int(alter,2)
                ans = r | alter
                break

    print(ans)
