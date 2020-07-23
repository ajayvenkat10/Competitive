t = int(input())

for i in range(t):
    line = input().split()
    pile1,pile2 = int(line[0]) , int(line[1])
    count = 0
    moves = 0
    while(True):
        moves+=1
        if(pile1 == pile2):
            count+=1
            break

        elif((pile1>pile2 and pile1 % pile2 == 0) or (pile2>pile1 and pile2 % pile1 == 0)):
            count += 1;
            break;

        else :

            flag = False
            if(pile1 > pile2):
                quotient = pile1//pile2

                if(moves==1 and quotient>1):
                    count+=1
                    break

                elif(quotient == 1):
                    pile1 = pile1-pile2

                else:
                    q = quotient
                    quotient = 1
                    while(quotient<=q):
                        x = pile2 * quotient
                        y = pile1 - x

                        if(max(y,pile2)//min(y,pile2) == 1):
                            pile1 = y
                            flag = True
                            break

                        quotient += 1

                    if(flag == False):
                        count+=1
                        break

            else:
                quotient = pile2//pile1

                if(moves==1 and quotient>1):
                    count+=1
                    break

                elif(quotient == 1):
                    pile2 = pile2-pile1

                else:
                    q = quotient
                    quotient = 1
                    while(quotient<=q):
                        x = pile1 * quotient
                        y = pile2 - x

                        if(max(y,pile1)//min(y,pile1) == 1):
                            pile2 = y
                            flag = True
                            break

                        quotient += 1

                    if(flag==False):
                        count+=1
                        break
            count += 1

    if(count%2 == 0):
        print("Rich")

    else:
        print("Ari")
