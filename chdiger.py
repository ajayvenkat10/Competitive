t = int(input())

for i in range(t):
    input_line = input().split()
    n = input_line[0]
    d = int(input_line[1])
    last_index = {}

    num_arr = list(map(int,list(n)))
    elements = list(set(num_arr))
    elements.sort()

    for i in range(len(num_arr)):
        last_index[num_arr[i]] = i

    start = 0
    end = 0
    ans = []

    if(d <= elements[0]):
        ans = [d]*len(num_arr)
    else:
        for i in range(len(elements)):
            end = last_index[elements[i]]
            if(end >= start):
                inter = []
                new = num_arr[start:end+1]
                inter = [elements[i]] * new.count(elements[i])
                ans.extend(inter)
                if(end == len(num_arr)-1):
                    break
                else:
                    start = end+1

    while(len(ans)<len(num_arr)):
        ans.append(d)

    for i in range(len(ans)):
        if(ans[i] > d):
            ans[i]=d

    ans = list(map(str,list(ans)))
    ans = ''.join(ans)
    ans = int(ans)
    print(ans)
