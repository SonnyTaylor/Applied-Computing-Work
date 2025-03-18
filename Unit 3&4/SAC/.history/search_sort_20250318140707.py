def quicksort(arr):
    # Base case: arrays with 0 or 1 element are already sorted
    if len(arr) <= 1:
        return arr
    else:
        # Choose a pivot element (here we use the last element)
        pivot = arr[-1]

        # Partition the array into two sub-arrays
        less_than_pivot = [x for x in arr[:-1] if x <= pivot]
        greater_than_pivot = [x for x in arr[:-1] if x > pivot]

        # Recursively sort the sub-arrays and concatenate with the pivot
        return quicksort(less_than_pivot) + [pivot] + quicksort(greater_than_pivot)
