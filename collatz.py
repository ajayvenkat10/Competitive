a=int(raw_input("Enter the number: "))

def red(n):
  if(n==1):
    return 0
  else:
    if(n%2==0):
      return 1 + red(n/2)
    else:
      return 1 + red(3*n+1)

print "Number of steps it takes to reach 1 is %d! " % (red(a))
