from collections import defaultdict


n = int(input())
word = list(map(int,input().split()))
dictionary = defaultdict(int)
dist_count = len(set(word))
count = 0
start = 0
start_index = 0
min_len = 1000000007
i = 0
j = n-1
count = 0
ans = 0
final = []
flag = 0
final = []
if(len(set(word)) == len(word)):
    print(0)
else:
    for i in range(n):
        for j in range(n):
            arr = []
            part1 = word[:i]
            part2 = word[j+1:]

            arr.extend(part1)
            arr.extend(part2)

            if(len(set(arr)) == len(arr) and len(set(arr))< dist_count):
                final.append(j-i)
    print(min(final))
    # while(i<j):
    #     dictionary[word[i]] += 1
    #     dictionary[word[j]] += 1
    #
    #     if(dictionary[word[i]] > 1 and dictionary[word[j]] > 1):
    #         if(word[i] == word[j]):
    #             if(dictionary[word[i]] == 2):
    #                 ans = j - i
    #             else:
    #                 ans = j - i + 1
    #
    #             final.append(ans)
    #
    #         else:
    #             ans = j - i + 1
    #             flag = 1
    #             break
    #
    #     elif(dictionary[word[i]] > 1):
    #         j -= 1
    #
    #     elif(dictionary[word[j]] > 1):
    #         i += 1
    #
    #     else:
    #         i += 1
    #         j -= 1
    #
    # if(flag or ans==0):
    #     print(ans)
    # else:
    #     print(min(final))
    # for i in range(len(word)):
    #     dictionary[word[i]] += 1
    #
    #     if(dictionary[word[i]] == 1):
    #         count += 1
    #
    #     if(count == dist_count):
    #         while(dictionary[word[start]] > 1):
    #             if(dictionary[word[start]] > 1):
    #                 dictionary[word[start]] -= 1
    #             start += 1
    #
    #         length_of_window = i - start + 1
    #
    #         if(length_of_window < min_len):
    #             min_len = length_of_window
    #             start_index =  start
    #
    # print(word[start_index:(start_index+length_of_window)])
    # print(length_of_window)
    # while(i<j):
    #     dictionary[word[i]] += 1
    #     dictionary[word[j]] += 1
    #
    #     if(dictionary[word[i]] > 1 and dictionary[word[j]] > 1):
    #         if(dictionary[word[i]] == 2):
    #             ans = j - i
    #         else:
    #             ans = j - i + 1
    #
    #         break
    #
    #     elif(dictionary[word[i]] > 1):
    #         j -= 1
    #
    #     elif(dictionary[word[j]] > 1):
    #         i += 1
    #
    #     else:
    #         i += 1
    #         j -= 1

        # if(dictionary[word[j]] < 1):
        #     dictionary[word[i]] += 1
        #     j -= 1
        #     count += 1
        #
        # if(dictionary[word[i]] == 1 and dictionary[word[i]] == 1 and dist_count == count):
        #     ans = j-i+1
        #     break

    # print(ans)

    # count = 0
    # pos = -1
    # for i in range(len(word)):
    #     dictionary[word[i]] += 1
    #
    #     if(dictionary[word[i]] == 2):
    #         count = dictionary[word[i]]
    #         pos = i
    #         break
    #
    # if(count == 1):
    #     print("None")
    #
    # else:
    #     print(word[pos])
