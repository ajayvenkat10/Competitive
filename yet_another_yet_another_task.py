def maxSubArraySum(a): 
  
    max_so_far = -3000000000
    max_ending_here = 0
    start = 0
    end = 0
    s = 0
  
    for i in range(len(arr)): 
  
        max_ending_here += a[i] 
  
        if max_so_far < max_ending_here: 
            max_so_far = max_ending_here 
            start = s 
            end = i 
  
        if max_ending_here < 0: 
            max_ending_here = 0
            s = i+1
  
    return start, end+1, max_so_far 

n = int(input())

arr = list(map(int, input().split()))

start, end, total = maxSubArraySum(arr)

print(total - max(arr[start:end]))