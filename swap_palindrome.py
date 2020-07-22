t = int(input())

for i in range(t):
    n = int(input())
    word = input()
    word = list(word)

    left = 0
    right = n-1

    swapped = [False]*len(word)

    flag = True

    while(left<right):
        if(word[left] != word[right]):
            if(left+1 == right ):
                flag = False 
                break

            if(not swapped[left] and word[left+1] == word[right]):
                word[left],word[left+1] = word[left+1], word[left]
                swapped[left] = True
                swapped[left + 1] = True

            elif(not swapped[right] and word[right-1] == word[left]):
                    word[right], word[right-1] = word[right-1], word[right]
                    swapped[right] = True
                    swapped[right - 1] = True
                
            else:
                flag = False
                break


        left += 1
        right -= 1 


    if(flag):
        print("YES")
        print(swapped.count(True)//2)

    else:
        print("NO")
