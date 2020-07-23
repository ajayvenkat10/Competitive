t = int(input())

for i in range(t):
    N = int(input())
    words = []
    time = []
    for i in range(N):
        word = input()
        x=2
        if word in words:
            words.append(word)
            time.append(time[words.index(word)]//2)
        else:
            for i in range(1,len(word)):
                if(abs(ord(word[i])-ord(word[i-1])) <= 2):
                    x+=4
                else:
                    x+=2

            words.append(word)
            time.append(x)

    print(sum(time))
