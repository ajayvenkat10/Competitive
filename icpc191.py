from collections import defaultdict

t = int(input())

for i in range(t):
    s,t = input().split()
    dict = defaultdict(int)
    word = s+t

    for i in range(len(word)):
        dict[word[i]] += 1

    arr = list(dict.values())

    odd = 0
    even = 0

    ans =  len(word)

    for i in range(len(arr)):
        if(arr[i] % 2):
            odd += 1

        else:
            even += 1

    if(len(word) % 2 == 0):
        if(even != len(arr)):
            ans += (odd - 1)

    else:
        ans += (odd-1)


    if(len(arr) == 1):
        ans = len(word)

    print(ans)
