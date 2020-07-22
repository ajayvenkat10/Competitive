n,q = map(int, input().split())

arr = list(map(int, input().split()))

prefix_sum = [bin(arr[0]).count('1')]

for i in range(1,n):
    prefix_sum.append( prefix_sum[i-1] + bin(arr[i]).count('1'))

prefix_sum.insert(0,0)

MAX = 10000000

for i in range(q):
    query = int(input())
    mini = MAX

    for i in range(n):
        pref = prefix_sum[i]

        low = i+1
        high = n

        while(low < high):

            mid = (low+high)//2

            if(prefix_sum[mid]-pref >= query):
                high = mid

            else:
                low = mid + 1

        if(prefix_sum[low]-pref >= query):
            mini = min(mini, low - i)

    if(mini == MAX):
        print(-1)
    else:
        print(mini)
        


