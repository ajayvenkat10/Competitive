t = int(input(""))

for i in range(t):
    n = int(input(""))
    observation_array = []
    observation = input("")

    observation_list = list(observation)

    for i in range(len(observation_list)):
        if(observation_list[i]=='H' or observation_list[i]=='T'):
            observation_array.append(observation_list[i])

    part1 = []
    part2 = []

    for i in range(0,len(observation_array),2):
        part1.append(observation_array[i])

    for i in range(1,len(observation_array),2):
        part2.append(observation_array[i])

    # print(part1)
    # print(part2)

    if(observation_array == [] or (set(part1)=={'H'} and set(part2)=={'T'} and (len(part1)==len(part2)))):
        print('Valid')

    else:
        print('Invalid')
