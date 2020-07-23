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

t = int(input(""))

for i in range(t):
    second_line = input("")
    second_line = second_line.split()
    N = int(second_line[0])
    K = int(second_line[1])
    answer_array = []
    sequence = []
    subsequence_array = []
    input_sequence = input("")
    input_sequence = input_sequence.split()
    ans = 1
    for i in range(N):
        sequence.append(int(input_sequence[i]))
    sequence.sort()
    printCombination(sequence,N,K)
    for i in range(len(subsequence_array)):
        # subsequence_array[i].sort()
        print(subsequence_array[i])
        subsequence_array[i] = subsequence_array[i][1:len(subsequence_array[i])-1]
        answer_array.extend(subsequence_array[i])

    sequence = sequence[1:len(sequence)-1]
    for i in range(len(sequence)):
        print(answer_array.count(sequence[i]))

    for i in range(len(answer_array)):
        ans = ans*answer_array[i]

    print(ans%(10**9+7))
