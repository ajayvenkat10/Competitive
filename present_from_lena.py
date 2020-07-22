t = int(input())

final = []

for i in range(0,t+1):
    each = [" "] * (t-i) 

    for j in range(i+1):
        each.append(j)

    for j in range(i-1, -1, -1):
        each.append(j)

    final.append(each)

part2 = final[:-1]
part2 = part2[::-1]

final.extend(part2)

for i in range(len(final)):
    print(* final[i])

 
