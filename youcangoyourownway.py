t = int(input())

for j in range(t):
    n = int(input())
    gpath = input()
    spath = ""

    for i in range(len(gpath)):
        if(gpath[i] == 'E'):
            spath += 'S'
        else:
            spath += 'E'

    print(("Case #%d: %s") % (j+1,spath))
