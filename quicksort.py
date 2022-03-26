array = [5, 12, 11, 10, -10, 2, -9, 84, 992, 91, 213]


# quick sort
def quicksort(arr, start, end):
    if (start < end):
        p = partition(arr, start, end)
        quicksort(arr, start, p - 1)
        quicksort(arr, p + 1, end)
    return arr


def partition(arr, start, end):
    pivot = arr[end]
    i = (start - 1)
    for j in range(start, end):
        if arr[j] < pivot:
            i+=1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[end] = arr[end], arr[i + 1]
    return i + 1

print("quicksort:")
print(array)
print(quicksort(array, 0, len(array) - 1))