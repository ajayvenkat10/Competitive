t = int(input())

for i in range(t):
    word = input()

    set_length = len(set(list(word)))

    ans = "YES"
    if(set_length <= 2):
        if(set_length == 1):
            ans = "YES"

        else:
            x = word[0]
            if(len(word)%2 == 0):
                for i in range(1, len(word)):
                    if(word[i] == x):
                        ans = "NO"
                        break
                        
                    x = word[i]
            else:
                ans = "NO"

    else:
        ans = "NO"

    print(ans)