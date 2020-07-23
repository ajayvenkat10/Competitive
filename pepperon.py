t = int(input())

for i in range(t):
    n = int(input())
    arr1 = []
    arr2 = []
    for i in range(n):
        pizza = input()
        part1 = pizza[:n//2]
        part2 = pizza[n//2:]
        arr1.append(part1.count('1'))
        arr2.append(part2.count('1'))

    initial = abs(sum(arr1) - sum(arr2))
    x= sum(arr1)
    y= sum(arr2)

    final = [initial]
    for i in range(len(arr1)):
        x1 = x
        y1 = y
        x1 = x1 - arr1[i] + arr2[i]
        y1 = y1 - arr2[i] + arr1[i]
        final.append(abs(x1-y1))
        
    print(min(final))
