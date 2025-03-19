import pytest
from search_sort import quicksort, binary_search


def test_quicksort_empty():
    assert quicksort([]) == []


def test_quicksort_single():
    assert quicksort([1]) == [1]


def test_quicksort_sorted():
    arr = [1, 2, 3, 4, 5]
    assert quicksort(arr) == [1, 2, 3, 4, 5]


def test_quicksort_reverse():
    arr = [5, 4, 3, 2, 1]
    assert quicksort(arr) == [1, 2, 3, 4, 5]


def test_quicksort_with_key():
    arr = [{"value": 3}, {"value": 1}, {"value": 4}, {"value": 2}]
    sorted_arr = quicksort(arr, key=lambda x: x["value"])
    assert [item["value"] for item in sorted_arr] == [1, 2, 3, 4]


def test_binary_search_empty():
    assert binary_search([], 1) == -1


def test_binary_search_single():
    assert binary_search([1], 1) == 0
    assert binary_search([1], 2) == -1


def test_binary_search_multiple():
    arr = [1, 2, 3, 4, 5]
    assert binary_search(arr, 1) == 0
    assert binary_search(arr, 3) == 2
    assert binary_search(arr, 5) == 4
    assert binary_search(arr, 6) == -1
