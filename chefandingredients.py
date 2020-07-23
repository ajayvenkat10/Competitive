T = int(input())
MAX = 1000000007
for i in range(T):
    n,k = input().split()
    n = int(n)
    k = int(k)
    answer = 0
    last_term = k-1

    if(n>=k):
        answer = last_term

    else:
        if(n == 2):
            answer = (last_term * (last_term+1))//2
        else:
            difference = n-1
            number_of_terms = last_term//difference + 1
            first_term = last_term - ((number_of_terms-1) * difference)
            sum_of_AP = (number_of_terms * (first_term + last_term))//2
            answer = sum_of_AP

    print(answer%(MAX))
