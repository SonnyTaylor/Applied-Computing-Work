def quicksort(array):
    if len(array) <= 1:
        return array
    # Choose a pivot. This example selects the last element
    pivot = array[-1]

    # Create three empty lists that will hold elements
    left = []  # Elements less than the pivot
    middle = []  # Elements equal to the pivot
    right = []  # Elements greater than the pivot

    # Partition the array based on the pivot
    for each in array:
        if each < pivot:
            left.append(each)
        elif each == pivot:
            middle.append(each)
        else:
            right.append(each)

    # Recursively sort the left and right sub-lists
    left_sorted = quicksort(left)
    right_sorted = quicksort(right)

    # Combine them: sorted left, pivot(s), sorted right
    return left_sorted + middle + right_sorted


# Example usage:
numbers = [10, 7, 8, 9, 1, 5]
sorted_numbers = quicksort(numbers)
print(sorted_numbers)

"""
PSEUDOCODE

BEGIN quicksort(array)
	IF LEN(array) <= 1 THEN
		RETURN array
	ENDIF
    
    pivot ← array[-1]
    left ← []
    middle ← []
    right ← []
    
    FOR each IN array DO
        IF each < pivot THEN
            APPEND each TO left
        ELSE IF each = pivot THEN
            APPEND each TO middle
        ELSE
            APPEND each TO right
        ENDIF
    ENDFOR
	
	left_sorted ← quicksort(left)
	right_sorted ← quicksort(right)
	
	RETURN left_sorted + middle + right_sorted
END
"""
