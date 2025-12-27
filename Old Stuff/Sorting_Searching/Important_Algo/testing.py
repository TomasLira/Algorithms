from selection_sort import selection_sort,selection_sort_rec
from insertion_sort import insertion_sort,insertion_sort_rec
from merge_sort import merge_sort_rec
from counting_sort import counting_sort
def test_sort():
    test_cases = [
        {
            "input": [64, 25, 12, 22, 11],
            "expected": [11, 12, 22, 25, 64],
        },
        {
            "input": [5, 1, 4, 2, 8],
            "expected": [1, 2, 4, 5, 8],
        },
        {
            "input": [20, 10, 30, 5, 15],
            "expected": [5, 10, 15, 20, 30],
        },
        {
            "input": [3, 3, 2, 1, 4],
            "expected": [1, 2, 3, 3, 4],
        },
        {
            "input": [1],
            "expected": [1],
        },
        {
            "input": [],
            "expected": [],
        },
    ]

    # Run tests
    for case in test_cases:
        # Change here to test different sorting algorithms
        result = counting_sort(case["input"].copy())
        assert result == case["expected"], f"Test failed for input {case['input']}. Expected {case['expected']}, but got {result}"
        print(f"Test passed for input {case['input']}. Result: {result}")

if __name__ == "__main__":
    test_sort()
