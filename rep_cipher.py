n = int(input())

encrypted  = input()

count = 1
start = 0
ans = ""
while(start<n):
    end = start + count
    word = encrypted[start:end]
    ans  = ans + word[0]
    count = count+1
    start = end 

print(ans)
