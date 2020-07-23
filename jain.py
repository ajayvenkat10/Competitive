t  =  int(input())

for i in range(t):
    n = int(input())
    d = {}
    initial = []
    for i in range(n):
        input_string = input()
        input_string = list(set(input_string))
        input_string.sort()
        input_string = ''.join(input_string)
        d[input_string] = 0
        initial.append(input_string)

    for i in range(len(initial)):
        d[initial[i]] += 1

    keys = list(d.keys())
    count = 0
    for i in range(len(keys)):
        for j in range(i+1,len(keys)):
            if(sorted(list(set(keys[i] + keys[j]))) == ['a','e','i','o','u']):
                count+= d[keys[i]] * d[keys[j]]

        if(keys[i] == "aeiou"):
            count += ((d[keys[i]]* (d[keys[i]]-1))//2)

    print(count)
