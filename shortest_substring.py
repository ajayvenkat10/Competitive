# def countkDist(str1, k):
#     n = len(str1)
#     res = 0
#     minimum = 100005
#     cnt = [0] * 27
#
#     for i in range(n):
#         dist_count = 0
#
#         cnt = [0] * 27
#
#         for j in range(i, n):
#             if(cnt[ord(str1[j]) - 97] == 0):
#                 dist_count += 1
#
#             cnt[ord(str1[j]) - 97] += 1
#
#             if(dist_count == k):
#                 minimum = min(minimum,len(str1[i:j+1]))
#                 break
#
#
#     return minimum
#
# # Driver Code
# if __name__ == "__main__":
#     str1 = "bcaacbc"
#     k = len(set(str1))
#     print(countkDist(str1, k))
import math
def minSum(num, k):
    num.sort(reverse = True)
    length = len(num)

    for i in range(k):
        index = i%length

        x = (num[index]/2)
        y = (num[index]//2)

        if(x-y < 0.5):
            num[index] = num[index]//2

        else:
            num[index] = (num[index]//2) + 1

    return(sum(num))

t = int(input())
for i in range(t):
    n = int(input())
    num = list(map(int, input().split()))
    k = int(input())

    print(minSum(num,k))
