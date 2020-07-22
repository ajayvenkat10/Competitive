from collections import defaultdict

def special_element(a, val):
    j = 0
    total_sum = 0

    for i in range(len(a)):
        total_sum += a[i]

        while(total_sum >= val and j < len(a)):
            
            if(total_sum == val and i - j >= 1):
                return True

            else:
                total_sum -= a[j]
                j += 1

    return False

t = int(input())

for i in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    special_elements = 0
    visited = defaultdict(bool)
    special = defaultdict(bool)

    for i in range(n):
        if(visited[arr[i]] == False):
            visited[arr[i]] = True 
            part1 = arr[:i]
            part2 = arr[i+1:]
            value = arr[i]
            if(special_element(part1, value) or special_element(part2, value)):
                special_elements += 1
                special[arr[i]] = True

        else:
            if(special[arr[i]] == True):
                special_elements += 1

    print(special_elements)
