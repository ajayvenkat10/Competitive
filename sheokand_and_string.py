def longest_common_prefix(seq1, seq2):
    start = 0
    while start < min(len(seq1), len(seq2)):
        if seq1[start] != seq2[start]:
            break
        start += 1
    return seq1[:start]

N = int(input(""))
set_of_strings = []
Results = []
for i in range(N):
    a = input("")
    set_of_strings.append(a)

Q = int(input(""))

for i in range(Q):
    parts_of_Q = input("")
    parts_of_Q = parts_of_Q.split()
    R = int(parts_of_Q[0])
    pattern_string = parts_of_Q[1]

    new_set_of_strings = set_of_strings[:R]
    new_set_of_strings.sort()
    lcp = longest_common_prefix(new_set_of_strings[0],pattern_string)
    ans = new_set_of_strings[0]

    for i in range(1,len(new_set_of_strings)):
        if(longest_common_prefix(new_set_of_strings[i],pattern_string) > lcp):
            lcp = longest_common_prefix(new_set_of_strings[i],pattern_string)
            ans = new_set_of_strings[i]

    print(ans)
