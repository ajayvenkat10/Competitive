first_line = input("")
first_line = first_line.split()
P = int(first_line[0])
S = int(first_line[1])
Ans = []
for item in range(P):

    subtask_scores = []
    successful_submissions = []
    input_line1 = input("")
    input_line1 = input_line1.split()

    input_line2 = input("")
    input_line2 = input_line2.split()

    tup = []
    for i in range(S):
        tup.append((int(input_line1[i]),int(input_line2[i])))

    tup.sort()

    for i in range(len(tup)):
        subtask_scores.append(tup[i][0])
        successful_submissions.append(tup[i][1])

    n = 0
    for i in range(len(successful_submissions)-1):
        if(successful_submissions[i]>successful_submissions[i+1]):
            n+=1

    Ans.append((n,item+1))

Ans.sort()

for i in range(len(Ans)):
    print(Ans[i][1])
