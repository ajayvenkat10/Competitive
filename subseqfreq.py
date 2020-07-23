# def MaxFreq(s):
#     n = len(s)
#     m = dict()
#
#     for i in range(n):
#         strng = ""
#         for j in range(i, n):
#             strng += s[j]
#             if strng in m.keys():
#                 m[strng] += 1
#             else:
#                 m[strng] = 1
#
#     maxi = 0
#
#     maxi_str = ""
#

#
#     return maxi_str

t = int(input())

for i in range(t):
    input_string = input()
    dict = {}
    for i in range(ord('a'),ord('z')+1):
        dict[chr(i)] =0
    for i in range(len(input_string)):
        dict[input_string[i]] += 1

    key  = dict.keys()
    values = dict.values()

    maxi = 0
    maxi_str = ""

    for i in dict:
        if dict[i] > maxi:
            maxi = dict[i]
            maxi_str = i
        elif dict[i] == maxi:
            ss = i
            if ss < maxi_str:
                maxi_str = ss

    print(maxi_str)
