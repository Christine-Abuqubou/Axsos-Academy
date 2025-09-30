def insertion_sort(arr):
    for i in range(1, len(arr)):
        current = arr[i]
        j = i - 1

        # Shift elements of arr[0..i-1], that are greater than current,
        # to one position ahead of their current position
        while j >= 0 and arr[j] > current:
            arr[j + 1] = arr[j]
            j -= 1

        # Place the current element into the correct position
        arr[j + 1] = current

    return arr
print(insertion_sort([5, 2, 3]))          