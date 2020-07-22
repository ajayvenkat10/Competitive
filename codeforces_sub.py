t = int(input())
a = 'codeforces'
ans = ""
frequency = [1]*10
i = 0
subs = 1

while(subs < t):

    subs = subs//frequency[i]
    frequency[i] += 1 
    subs *= frequency[i]
    i = (i+1) % 10

for i in range(10):
    ans += a[i] * frequency[i]

print(ans)
