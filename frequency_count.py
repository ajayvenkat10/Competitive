def findCounts(arr, n):
    result = {}
    i = 0
    while i<n:

        if arr[i] <= 0:
            i += 1
            continue

        elementIndex = arr[i] - 1

        if arr[elementIndex] > 0:
            arr[i] = arr[elementIndex]

            arr[elementIndex] = -1

        else:
            arr[elementIndex] -= 1
            arr[i] = 0
            i += 1

    for i in range(0,n):
        result[i+1] = abs(arr[i])

    return(result)


# Driver program to test above function
arr = [2, 3, 3, 2, 5]
new = findCounts(arr, len(arr))
# print(new)

arr1 = [1]
findCounts(arr1, len(arr1))

arr3 = [4, 4, 4, 4]
findCounts(arr3, len(arr3))

# arr2 = [7,8,9,10,11]
# print(findCounts(arr2, len(arr2)))

arr4 = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]
findCounts(arr4, len(arr4))

arr5 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
findCounts(arr5, len(arr5))

arr6 = [11, 9, 8, 7, 6, 5, 4, 3, 2, 1]
print(findCounts(arr6, len(arr6)))
