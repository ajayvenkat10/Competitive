# t = int(input())
# stack1 = []
# # stack2 = []
# greatest = 0
# for i in range(t):
#     line = input().split()
#     if(int(line[0]) == 1):
#         x = int(line[1])
#         if(x>greatest):
#             stack1.append(2*x - greatest)
#             greatest = x
#         else:
#             stack1.append(x)
#
#     elif(int(line[0]) == 2):
#         y = stack1.pop()
#         if(y > greatest):
#             greatest = 2*greatest - y
#
#     else:
#         print(greatest)

def isBalanced(s):
    ans = 'YES'
    stack = []
    for i in range(len(s)):
        if(s[i] == '(' or s[i] == '{' or s[i]== '['):
            stack.append(s[i])

        else:
            x = stack.pop()
            if(s[i]==')'):
                if(x != '('):
                    ans = 'NO'
                    break
            elif(s[i]=='}'):
                if(x != '{'):
                    ans = 'NO'
                    break
            else:
                if(x != '['):
                    ans = 'NO'
                    break

    return(ans)

print(isBalanced("{[()]}"))
