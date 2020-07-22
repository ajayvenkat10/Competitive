n = input()

lucky_digits = 0
for letter in n:
    if(letter == '4' or letter == '7'):
        lucky_digits += 1

flag = True 
lucky_digits = str(lucky_digits)

for num in lucky_digits:
    if(num == '4' or num=='7'):
        flag = True 

    else:
        flag = False
        break         

if(flag):
    print("YES")

else:
    print("NO")

