MAX = 250001


class BinaryIndexedTree:

    BITree = []

    def __init__(self, size):
        self.size = size + 2
        self.BITree = [0] * self.size

    def query(self, index):
        index += 1
        ans = 0

        while(index >= 1):
            ans += self.BITree[index]
            index -= index & (-index)

        return ans

    def update(self, index, value):
        index += 1

        while(index <= n):
            self.BITree[index] += value
            index += index & (-index)

    def LRquery(self, left, right):
        return self.query(right) - self.query(left-1)


def countOfSubarrays():
    li = []

    for _ in range(n):
        li.append([])

    tree_obj = BinaryIndexedTree(n+2)

    stack = []

    for i in range(n):
        while(len(stack) != 0 and arr[stack[-1]] <= arr[i]):
            stack.pop()

        if(len(stack) == 0):
            tree_obj.update(i, 1)

        else:
            li[stack[-1]].append(i)

        stack.append(i)

    stack = []
    next_greatest = [0]*MAX

    for i in range(n-1, -1, -1):
        while(len(stack) != 0 and arr[stack[-1]] >= arr[i]):
            stack.pop()

        if(len(stack) == 0):
            next_greatest[i] = n

        else:
            next_greatest[i] = stack[-1]

        stack.append(i)

    valid_subarrays = 0

    for i in range(n):
        for j in li[i]:
            tree_obj.update(j, 1)

        valid_subarrays += tree_obj.LRquery(i, next_greatest[i]-1)
        tree_obj.update(i, -1)

    return valid_subarrays


t = int(input())

for i in range(t):
    n = int(input())
    arr = list(map(int, input().split()))

    answer = 0
   
    answer += countOfSubarrays()
    arr.reverse()
    answer += countOfSubarrays()

    count_duplicate = 1

    for i in range(1, n):
        if(arr[i] != arr[i-1]):
            answer -= (count_duplicate * (count_duplicate+1))//2
            count_duplicate = 1

        else:
            count_duplicate += 1

    answer -= (count_duplicate * (count_duplicate+1))//2

    print(answer)
