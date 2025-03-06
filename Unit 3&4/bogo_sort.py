import random


def is_sorted(arr):
    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            return False
    return True


def bogo_sort(arr):
    while not is_sorted(arr):
        random.shuffle(arr)
    return arr


# Example usage
if __name__ == "__main__":
    arr = [3, 2, 5, 1, 4]
    print("Unsorted array:", arr)
    sorted_arr = bogo_sort(arr)
    print("Sorted array:", sorted_arr)
