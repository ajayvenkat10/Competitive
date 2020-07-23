from collections import defaultdict

t = int(input())

for i in range(t):
    S = input()
    R = input()

    dict1 = defaultdict(int)
    dict2 = defaultdict(int)

    for i in range(len(S)):
        dict1[S[i]] += 1

    for i in range(len(R)):
        dict2[R[i]] += 1

    first = list(dict1.keys())
    second = list(dict2.keys())

    inter = list(set(first) & set(second))
    if(len(inter) == 0):
        print("Impossible")

    else:
        flag = 1
        ans = ""
        for i in range(len(inter)):
            if(dict1[inter[i]] > dict2[inter[i]]):
                flag = 0
                break
            else:
                dict2[inter[i]] -= dict1[inter[i]]

        if(flag):
            final = S
            part1 = ''.join(['a']*dict2['a'])
            part2 = ''.join(['b']*dict2['b'])
            if(S[0] == 'a'):
                ans = part1 + final + part2

            else:
                ans = part1 + part2 + final

            print(ans)
        else:
            print("Impossible")
