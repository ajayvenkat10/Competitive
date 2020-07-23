def print_ans(ans):
    print(ans, flush=True)

t = int(input())

for i in range(t):
    n = int(input())
    a = int(input())
    nperf = 10**n
    s = 2 * nperf + a
    print_ans(s)
    b = int(input())
    c = nperf - b
    print_ans(c)
    d = int(input())
    e = nperf - d
    print_ans(e)
    result = int(input())

    if(result == -1):
        break
