t = int(input())

for i in range(t):
    arr = input()
    count = 0
    pos = 0
    dots = 0
    digit = 0
    a = []
    b = []
    ans = True
    for i in range(len(arr)):
        if(arr[i] == "."):
            dots+=1
        if(arr[i].isdigit()):
            digit+=1

    if(digit <= 1):
        print("safe")

    else:
        for i in range(len(arr)):
            if(arr[i].isdigit()):
                pos = i
                break

        for i in range(pos,len(arr)):
            if(arr[i].isdigit()):
                a.append(int(arr[i]))
                b.append(i)

        for i in range(len(a)-1):
            if(b[i+1] - b[i] <= a[i]+a[i+1]):
                ans = False
                break

        if(ans):
            print("safe")

        else:
            print("unsafe")
