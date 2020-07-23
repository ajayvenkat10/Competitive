def swap(s1,s2):
    return s2,s1

def quicksort(A, l, r):
    if l < r:
        p = partition(A, l, r)
        quicksort(A, l, p-1)
        quicksort(A, p+1, r)
    return A

def partition(A, l, r):
    p = A[l]
    i = l+1
    j = r
    done = False
    while not done:
        while i <= j and A[i] <= p:
            i=i+1
        while A[j] >= p and j >=i:
            j=j-1
        if j < i:
             done = True
        else:
            A[i],A[j]=swap(A[i],A[j])
    A[l],A[j]=swap(A[l],A[j])
    return j

print "Enter the number of elements in the array: "
n=int(raw_input(""))
print "Enter the array elements"
A=[]
x=raw_input("")
x=x.split()

for i in range(n):
    b=int(x[i])
    A.append(b)

A=quicksort(A,0,len(A)-1)
print "The sorted array is: "
print A
