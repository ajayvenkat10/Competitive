t = int(input())

for i in range(t):
    N = int(input())

    initial = input().split()
    final = input().split()

    initial_array = []
    final_array = []

    for i in range(N):
        initial_array.append(int(initial[i]))
        final_array.append(int(final[i]))

    
