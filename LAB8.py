def mergeSort(list):
    if len(list) < 2:
        return list
    middle = int(len(list) / 2)
    left = mergeSort(list[:middle])
    right = mergeSort(list[middle:])
    return merge(left, right)

def merge(left, right):
    if not len(left) or not len(right):
        return left or right
    result = []
    i, j = 0, 0
    while (len(result) < len(left) + len(right)):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
        if i == len(left) or j == len(right):
            result.extend(left[i:] or right[j:])
            break
    return result

def inside(arr, low, high):
    i = (low - 1)
    for j in range(low, high):
        if (arr[j] <= arr[high]):
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return (i + 1)

def inside2(arr, low, high):
    i = low - 1
    j = high + 1
    while (True):
        i += 1
        while (arr[i] < arr[low]):
            i += 1
        j -= 1
        while (arr[j] > arr[low]):
            j -= 1
        if (i >= j):
            return j
        arr[i], arr[j] = arr[j], arr[i]

def quickSort(arr, low, high):
    if (low < high):
        pi = inside(arr, low, high)
        quickSort(arr, low, pi - 1)
        quickSort(arr, pi + 1, high)

arr = [29,10,14,37,14,20,7,16,12]
print("Array old:",arr)
print("============== Merge sort =============")
arr = [29,10,14,37,14,20,7,16,12]
print(mergeSort(arr))
print("============== Lomuto Quicksort =============")
arr = [29,10,14,37,14,20,7,16,12]
quickSort(arr, 0, len(arr) - 1)
print(arr)
print("============== Hoare Quicksort =============")
arr = [29,10,14,37,14,20,7,16,12]
n = len(arr)
quickSort(arr, 0, n - 1)
print(arr)


