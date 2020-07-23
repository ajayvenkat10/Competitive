from fractions import gcd
Universal = []
MAX = 1000000000
a = 3
b = 7
def SieveOfEratosthenes(n):
    count=0
    prime = [True for i in range(n+1)]
    p = 2
    while (p * p <= n):
        if (prime[p] == True):
            for i in range(p * p, n+1, p):
                prime[i] = False
        p += 1

    for p in range(2, n):
        if prime[p]:
            Universal.append(p)

SieveOfEratosthenes(700000)

t = int(input())

for i in range(t):
    n = int(input())
    sequence = []

    i=0
    j=1

    if(n==4):
        print("6 10 35 21")

    elif(n==5):
        print("6 10 55 77 21")

    elif(n==6):
        print("6 10 55 77 91 39")

    elif(n==8):
        print("6 10 55 77 91 143 187 51")

    else:
        final = []
        while(n>0):
            value = Universal[i]*Universal[j]
            if(value>MAX):
                i = a
                j = b
                b = b+3

                inter = sequence[-1]//gcd(sequence[-1],sequence[-2])
                sequence.append(inter*Universal[i])
                sequence.append(Universal[i]*Universal[j])
                i+=1
                final.extend(sequence)
                sequence = []
                n=n-1

            else:
                sequence.append(value)
                if(len(sequence) %2 == 1):
                    j+=1
                else:
                    i+=1
            n-=1

        final.extend(sequence)

        final[-1] = gcd(final[-1],final[-2]) * 3

        print(*final)
