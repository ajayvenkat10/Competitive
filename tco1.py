# # from collections import defaultdict
# class EllysCodeConstants:
#     def getLiteral(name):
#         suffix  = ['L', 'LL', 'U', 'UL', 'ULL', 'LU', 'LLU']
#         valid = { 'O': '0', 'I':'1' , 'Z': '2' , 'S': '5' , 'T':'7'}
#         valid_list = list(valid.keys())
#         ans = "0x"
#         # name = list(name)
#         for i in range(len(name)):
#             if(name[i] == 'L' or name[i] == 'U'):
#                 if name[i:] in suffix:
#                     ans += name[i:]
#
#                 else:
#                     ans = ""
#                 break
#
#             else:
#                 if(ord(name[i]) <= 70):
#                     ans += name[i]
#
#                 elif name[i] in valid_list:
#                     ans += valid[name[i]]
#
#                 else:
#                     ans = ""
#                     break
#
#         return(ans)
#
#     print(getLiteral("FLU"))

t=int(input())
for i in range(0,t):
    string=input()
    x=str()
    all_freq={}
    for i in string:
        if i in all_freq:
            all_freq[i]+=1
        else:
            all_freq[i]=1

    print(all_freq)
    for i in all_freq:
        y=i+str(all_freq[i])
        x=x+y

    print(x)
    length=len(string)
    lengthModified=len(x)
    if(lengthModified < length):
        print("YES")
    else:
        print("NO")
