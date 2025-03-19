def quicksort(arr, key=None):
    # Base case: arrays with 0 or 1 element are already sorted
    if len(arr) <= 1:
        return arr
    else:
        # Choose a pivot element (here we use the last element)
        pivot = arr[-1]
        pivot_value = key(pivot) if key else pivot

        # Partition the array into two sub-arrays
        less_than_pivot = [x for x in arr[:-1] if (key(x) if key else x) <= pivot_value]
        greater_than_pivot = [
            x for x in arr[:-1] if (key(x) if key else x) > pivot_value
        ]

        # Recursively sort the sub-arrays and concatenate with the pivot
        return (
            quicksort(less_than_pivot, key)
            + [pivot]
            + quicksort(greater_than_pivot, key)
        )


def binary_search(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        # Check if target is present at mid
        if arr[mid] == target:
            return mid

        # If target is greater, ignore left half
        elif arr[mid] < target:
            left = mid + 1

        # If target is smaller, ignore right half
        else:
            right = mid - 1

    # Target is not present in the array
    return -1
