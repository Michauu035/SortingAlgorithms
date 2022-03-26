array = [10 ,23, 34, 431, 123, 9213, 123, 1, 0 ,23, 2]

# bubble sort
def bubblesort(arr):
    for i in range(0, len(arr)-1):
        for j in range(0, len(arr) - 1):
            if(arr[j] > arr[j+1]):
                arr[j], arr[j+1] = arr[j+1], arr[j]

    return arr

print("bubblesort: ")
print(array)
print(bubblesort(array))