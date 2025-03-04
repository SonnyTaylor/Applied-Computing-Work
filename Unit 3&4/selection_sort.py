"""
BEGIN
    FUNCTION selection_sort(arr):
        n = LENGTH(arr)

        FOR i FROM 0 TO n - 1:
            min_index = i

            FOR j FROM i + 1 TO n - 1:
                IF arr[j] < arr[min_index]:
                    min_index = j

            IF min_index ≠ i:
                temp = arr[i]
                arr[i] = arr[min_index]
                arr[min_index] = temp

        RETURN arr
END
"""
