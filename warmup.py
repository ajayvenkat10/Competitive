subsequence_array=[]
def combinationUntil(arr,data,start,end,index,r):
    i = 0
    subsequence = []
    if(index == r):
        for j in range(r):
            subsequence.append(data[j])
        subsequence_array.append(subsequence)
        return

    for i in range(start,end+1):
        if(end-i+1 >= r-index):
            data[index] = arr[i]
            combinationUntil(arr,data,i+1,end,index+1,r)

def printCombination(arr,n,r):
    data = []
    for i in range(r):
        data.append(0)
    combinationUntil(arr,data,0,n-1,0,r)


n = int(input(""))

A = []

arr = input("")
arr = arr.split()

for i in range(n):
    A.append(int(arr[i]))

for i in range(1,len(A)+1):
    printCombination(A,len(A),i)

print(subsequence_array)
# for i in range(len(subsequence_array)):
#     subsequence_array[i] = sum(subsequence_array[i])
#
# print(len(set(subsequence_array)))
