import pytest
from array_cli_tool import generate_random_array, merge_sort, quick_sort, time_operation

def test_generate_random_array():
    arr = generate_random_array(10, 1, 100)
    assert len(arr) == 10
    assert all(1 <= x <= 100 for x in arr)

def test_merge_sort():
    arr = [3, 1, 4, 1, 5, 9]
    sorted_arr = merge_sort(arr)
    assert sorted_arr == sorted(arr)

def test_quick_sort():
    arr = [3, 1, 4, 1, 5, 9]
    sorted_arr = quick_sort(arr)
    assert sorted_arr == sorted(arr)

def test_time_operation():
    arr = [3, 1, 4, 1, 5, 9]
    sorted_arr, elapsed_time = time_operation(merge_sort, arr)
    assert sorted_arr == sorted(arr)
    assert isinstance(elapsed_time, str)
