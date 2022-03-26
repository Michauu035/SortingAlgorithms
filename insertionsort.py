array = [92, 123, 43, 34, 16, 189, 231, 13, 0, 3, -5, 12]


# insertion sort
def insertionsort(arr):
    for i in range(1, len(arr)):
        j = i - 1
        key = arr[i]
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

    return arr

print("insertion sort: ")
print(array)
print(insertionsort(array))