import math

class Node:
    def __init__(self,key):
        self.left = None
        self.right = None
        self.data = key
        self.lCount = 0

def insert_node(root,node):
    pTraverse =  root
    currentParent = root

    while(pTraverse):
        currentParent = pTraverse

        if(node.data < pTraverse.data):
            pTraverse.lCount+=1
            pTraverse = pTraverse.left
        else:
            pTraverse = pTraverse.right

    if(root == None):
        root = node
    elif( node.data < currentParent.data ):
    	currentParent.left = node
    else:
    	currentParent.right = node
    return(root)

def binary_search_tree(root,keys,size):
    new_node = None
    iterator = 0
    for iterator in range(size):
        new_node = Node(keys[iterator])

        root = insert_node(root,new_node)

    return(root)

def k_smallest_element(root,k):
    ret = -1

    if(root):
        pTraverse = root

    while(pTraverse):
        if( (pTraverse.lCount + 1) == k ):
            ret = pTraverse.data
            break

        elif( k > pTraverse.lCount ):
            k = k - (pTraverse.lCount + 1)
            pTraverse = pTraverse.right

        else:
            pTraverse = pTraverse.left

    return (ret)

t = int(input())

for i in range(t):
    line1 = input().split()
    n,k = int(line1[0]),int(line1[1])
    arr = []
    line = input().split()
    for i in range(n):
        arr.append(int(line[i]))

    flag = 0
    j = 0
    for i in range(n-1):
        if(arr[i]>arr[i+1]):
            flag = 1
            break
    count = 0
    kth_ele = 0

    if(flag==0):
        for i in range(n):
            sub_arr_per_i = []
            count_arr_per_i = [0] * 2001
            for j in range(i,n):
                sub_arr_per_i.append(arr[j])
                count_arr_per_i[arr[j]] += 1
                m = math.ceil(k/len(sub_arr_per_i))
                index = math.ceil(k/m) -1

                x = count_arr_per_i[sub_arr_per_i[index]]

                if(count_arr_per_i[x]):
                    count+=1
    else:
        for i in range(n):
            sub_arr_per_i = []
            count_arr_per_i = [0]*2001
            root = None
            for j in range(i,n):
                sub_arr_per_i.append(arr[j])
                count_arr_per_i[arr[j]] += 1
                m = math.ceil(k/len(sub_arr_per_i))
                index = math.ceil(k/m)

                new_node = Node(arr[j])
                root = insert_node(root,new_node)

                kth_ele = k_smallest_element(root,index)
                x = count_arr_per_i[kth_ele]

                if(count_arr_per_i[x]):
                    count+=1

    print(count)
