# This script implements a binary search algorithm that returns the original index of the target element in the array.
def binary_search_original_index(array, target):
    # Create a list of tuples (value, original_index)
    indexed_array = [(value, idx) for idx, value in enumerate(array)]
    # Sort based on the value
    indexed_array.sort(key=lambda x: x[0])
    
    left, right = 0, len(indexed_array) - 1
    while left <= right:
        mid = (left + right) // 2
        if indexed_array[mid][0] == target:
            return indexed_array[mid][1]  # Return original index
        elif indexed_array[mid][0] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

# Example usage
if __name__ == "__main__":
    numbers = [5, 2, 9, 1, 5, 6]
    target = 2

    index = binary_search_original_index(numbers, target)
    if index != -1:
        print(f"Element {target} found at original index {index}.")
    else:
        print(f"Element {target} not found in the array.")
