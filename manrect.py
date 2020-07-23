def query(a,b):
    print("Q"," ",a," ",b, flush=True)
    dist = int(input())
    return(dist)
max = 1000000000

t =  int(input())

for i in range(t):
    d1 = query(0,0)
    d2 = query(max,0)

    mid_point = (d1+max-d2)//2

    yl = query(mid_point,0)
    xl = d1-yl

    xu = max-d2+yl

    d3 = query(max,max)
    yu = (2*max) - xu - d3

    print("A"," ",xl," ",yl," ",xu," ",yu)

    ans=int(input())
    if(ans!=1):
        break
