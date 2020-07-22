t = int(input())

for i in range(t):
    n = input()

    ans = []
    for i in range(len(n)):
        if(n[i] != '0'):
            ans.append(int(n[i]) * pow(10, len(n) - i - 1))

    print(len(ans))
    print(* ans)