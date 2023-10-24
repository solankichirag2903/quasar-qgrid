def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        # Flag to optimize the algorithm by checking if any swaps are made in a pass.
        # If no swaps are made, the list is already sorted, and we can break early.
        swapped = False

        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                # Swap the elements
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True

        # If no swaps were made in a pass, the list is sorted, and we can break.
        if not swapped:
            break

# Example usage:
arr = [64, 34, 25, 12, 22, 11, 90]
bubble_sort(arr)
print("Sorted array is:", arr)
