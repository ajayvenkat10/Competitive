n, k, l, c, d, p, nl, np = map(int, input().split())

part1 = (k * l)//nl 
part2 = c * d
part3 = p // np 

print(min(part1, part2, part3)//n)