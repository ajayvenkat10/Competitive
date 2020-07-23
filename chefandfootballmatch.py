t = int(input())

for i in range(t):
    n = int(input())

    favorite = 0
    opposition = 0

    for i in range(n):
        q,a,b = map(int, input().split())

        if(q==1):
            favorite = a
            opposition = b
            print("YES")

        else:
            if(a==b):
                favorite,opposition = a,b
                print("YES")

            else:
                if(favorite!=opposition and min(favorite,opposition) == min(a,b) and max(favorite,opposition) == max(a,b)):
                    print("YES")

                elif(min(a,b) < favorite and max(a,b) > favorite):
                    favorite = max(a,b)
                    opposition = min(a,b)
                    print("YES")

                elif(min(a,b) == favorite and max(a,b) > favorite and favorite!=opposition):
                    if(opposition< min(a,b) and opposition< max(a,b)):
                        print("NO")
                    else:
                        favorite = min(a,b)
                        opposition = max(a,b)
                        print("YES")

                elif(min(a,b) < favorite and max(a,b) == favorite and favorite!=opposition):
                    favorite = max(a,b)
                    opposition = min(a,b)
                    print("YES")

                elif(min(a,b) == opposition and max(a,b) > opposition and favorite!=opposition):
                    if(favorite< min(a,b) and favorite< max(a,b)):
                        print("NO")

                    else:
                        favorite = max(a,b)
                        opposition = min(a,b)
                        print("YES")

                elif(min(a,b) < opposition and max(a,b) == opposition and favorite!=opposition):
                    favorite = min(a,b)
                    opposition = max(a,b)
                    print("YES")

                elif(min(a,b) < opposition and max(a,b) > opposition):
                    opposition = max(a,b)
                    favorite = min(a,b)
                    print("YES")

                else:
                    print("NO")
