def binarySearch (arr, l, r, x):

    while(l <= r):
        mid = (l + r) //2

        if arr[mid] == x:
            return(True)
        elif arr[mid] > x:
            r = mid-1
        else:
            l = mid+1

    return(False)

t = int(input())

for i in range(t):
    Universal =[]
    N = int(input())
    Elements_array = []
    Elements = input()
    Elements = Elements.split()
    even = 0
    odd = 0
    for_zero = 0
    ans = 0
    final = 0
    xor_zero = 0
    xor_two = 0
    for i in range(N):
        Elements_array.append(int(Elements[i]))

    Elements_set = list(set(Elements_array))
    Elements_set.sort()
    for i in range(max(Elements_array)+1):
        Universal.append(0)

    for i in range(len(Elements_array)):
        Universal[Elements_array[i]]+=1

    for i in range(len(Elements_array)):
        if(Elements_array[i]%2==0):
            even += 1
        else:
            odd += 1

    for i in range(len(Elements_set)):
        for_two = 0
        part_a = Universal[Elements_set[i]]
        for_zero = int((part_a * (part_a-1))/2)
        xor_zero += for_zero

        if(binarySearch(Elements_set,i+1,len(Elements_set)-1,(Elements_set[i]^2))):
            part_b = Universal[Elements_set[i]^2]
            for_two = (part_a * part_b)

        xor_two += for_two

    final = int((N*(N-1))/2)-(even*odd)-(xor_zero)-(xor_two)

    print(final)
