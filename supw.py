N = int(input())
hours = list(map(int, input().split()))
best =[]

if(N < 3):
    print(0)

else:
    best.extend(hours[:3])
    for i in range(3,N):
        best.append(hours[i] + min( best[ i-3:]))
    print(min(best[len(best)-3 : ]))
