def printSubsequences(arr, index, subarr, count): 
    # Print the subsequence when reach  
    # the leaf of recursion tree 
    if index == len(arr): 
          
        # Condition to avoid printing 
        # empty subsequence 
        if len(subarr) != 0: 
            if(abs(max(subarr) - min(subarr)) == abs(subarr[0] - subarr[-1])):
                count += 1             
      
    else: 
        # Subsequence without including  
        # the element at current index 
        printSubsequences(arr, index + 1, subarr, count) 
          
        # Subsequence including the element 
        # at current index 
        printSubsequences(arr, index + 1, 
                            subarr+[arr[index]], count) 
      
    return count 

t = int(input())

for i in range(t):
    n = int(input())
    arr = list(map(int, input().split()))

    count = 0
    

    print(printSubsequences(arr, 0, [], 0))