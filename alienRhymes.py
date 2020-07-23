from collections import defaultdict
t = int(input())

for k in range(t):
    n = int(input())
    words = []
    for i in range(n):
        word = input()
        words.append(word)

    dict = defaultdict(int)
    prefix_set = []
    for i in range(n):
        for j in range(len(words[i])-1,-1,-1):
            prefix = words[i][j:]
            print(prefix)
            dict[prefix] += 1
            if(dict[prefix] >= 2):
                if prefix not in prefix_set:
                    prefix_set.append(prefix)

    print(("Case #%d: %d") % (k+1,len(prefix_set) * 2))
