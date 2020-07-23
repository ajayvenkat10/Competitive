t = int(input())

for i in range(t):
    N = int(input())

    ans=True
    temple_strips_list = []
    temple_strips = input()
    temple_strips = temple_strips.split()
    for i in range(N):
        temple_strips_list.append(int(temple_strips[i]))

    if(N%2==0 or temple_strips_list[0]!=1 or temple_strips_list[0]!=temple_strips_list[-1]):
        ans = False

    else:
        mid = temple_strips_list[len(temple_strips_list)//2]

        if(mid == max(temple_strips_list)):
            part1 = temple_strips_list[:len(temple_strips_list)//2]
            part2 = temple_strips_list[(len(temple_strips_list)//2)+1:]

            for i in range(1,(len(temple_strips_list)//2)+1):
                if(temple_strips_list[i]-temple_strips_list[i-1]!=1):
                        ans=False
                        break

            if(part1!=part2[::-1]):
                ans = False

        else:
            ans = False

    if(ans):
        print("yes")

    else:
        print("no")
