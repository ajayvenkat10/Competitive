t = int(input())

for i in range(t):
    n,k = map(int, input().split())

    arr = list(map(int, input().split()))

    odd = 0
    even = 0

    for i in range(n):
        if(arr[i]%2 == 1):
            odd += 1

        else:
            even += 1

    if(k > n or odd == 0):
        ans = "No"
    
    else:
        odd -= 1
        
        k-=1

        if(k % 2 == 0):
            if(odd >= k):
                ans = "Yes"
            else:
                if(odd % 2 == 0):
                    if(even >= k-(odd)):
                        ans = "Yes"
                    else:
                        ans = "No"
                else:
                    if(even >= k - (odd -1)):
                        ans = "Yes"

                    else:
                        ans = "No"

        else:
            if(odd >= k):
                if(even >= 1):
                    ans = "Yes"
                else:
                    ans = "No"

            else:
                if(odd % 2 == 0):
                    if(even >= k-(odd)):
                        ans = "Yes"
                    else:
                        ans = "No"

                else:
                    if(even >= k-(odd -1)):
                        ans = "Yes"

                    else:
                        ans = "No"
            

    print(ans)