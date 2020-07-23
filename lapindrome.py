t = int(input())

for i in range(t):
    word = input()
    mid = len(word)//2
    word = list(word)
    if(len(word)%2 == 0):
        part1 = word[:mid]
        part2 = word[mid:]

    else:
        part1 = word[:mid]
        part2 = word[mid+1:]

    if(sorted(part1) == sorted(part2)):
        print("YES")
    else:
        print("NO")
