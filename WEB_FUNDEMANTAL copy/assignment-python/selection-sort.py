def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        # Assume the smallest value is at position i
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        # Swap the found minimum with the current position
        arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr