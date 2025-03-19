def quicksort(arr, key=None):
    """
    Implements the QuickSort algorithm to sort an array.

    Args:
        arr: The array to be sorted
        key: Optional function to extract comparison key from elements

    Returns:
        Sorted array using the QuickSort algorithm
    """
    # Base case: arrays with 0 or 1 element are already sorted
    if len(arr) <= 1:
        return arr
    else:
        # Choose a pivot element (here we use the last element)
        pivot = arr[-1]
        # Extract comparison value using key function if provided, otherwise use element directly
        pivot_value = key(pivot) if key else pivot

        # Partition the array into two sub-arrays based on pivot
        # Elements less than or equal to pivot go to left sub-array
        less_than_pivot = [x for x in arr[:-1] if (key(x) if key else x) <= pivot_value]
        # Elements greater than pivot go to right sub-array
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
    """
    Implements binary search algorithm to find target in sorted array.

    Args:
        arr: Sorted array to search in
        target: Value to find

    Returns:
        Index of target if found, -1 if not found
    """
    # Initialize search boundaries
    left, right = 0, len(arr) - 1

    while left <= right:
        # Calculate middle point
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
