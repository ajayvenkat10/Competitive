#!/bin/python3

import os
import sys

#
# Complete the equalStacks function below.
#
def equalStacks(h1, h2, h3):
    #
    # Write your code here.
    #
    sum1 = sum(h1)
    sum2 = sum(h2)
    sum3 = sum(h3)
    while(True):

        if(min(sum1,sum2,sum3) == 0):
            x = 0
            break
        elif(sum1 == sum2 and sum2 == sum3):
            x= sum1
            break
        else:
            if sum1>=sum2 and sum1>=sum3:
                sum1 -= h1[0]
                h1.pop(0)
            elif sum2>=sum1 and sum2>=sum3:
                sum2 -= h2[0]
                h2.pop(0)
            else:
                sum3 -= h3[0]
                h3.pop(0)
    return(x)

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n1N2N3 = input().split()

    n1 = int(n1N2N3[0])

    n2 = int(n1N2N3[1])

    n3 = int(n1N2N3[2])

    h1 = list(map(int, input().rstrip().split()))

    h2 = list(map(int, input().rstrip().split()))

    h3 = list(map(int, input().rstrip().split()))

    result = equalStacks(h1, h2, h3)
    print(result)
    # fptr.write(str(result) + '\n')

    # fptr.close()
