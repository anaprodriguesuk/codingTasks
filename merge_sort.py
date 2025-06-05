def merge_sort_by_length(arr):
    if len(arr) <= 1:
        return arr

    # Divide the array into two halves
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    # Recursively sort each half
    left_half = merge_sort_by_length(left_half)
    right_half = merge_sort_by_length(right_half)

    # Merge the sorted halves
    return merge_by_length(left_half, right_half)

def merge_by_length(left, right):
    result = []
    left_index = 0
    right_index = 0

    # Merge the two halves while comparing string lengths
    while left_index < len(left) and right_index < len(right):
        if len(left[left_index]) > len(right[right_index]):
            result.append(left[left_index])
            left_index += 1
        else:
            result.append(right[right_index])
            right_index += 1

    # Add any remaining elements from the left and right halves
    result.extend(left[left_index:])
    result.extend(right[right_index:])
    
    return result

# Example usage
string_list = ["apple", "banana", "orange", "kiwi", "strawberry", "grape", "watermelon", "pineapple", "blueberry", "mango"]
sorted_strings = merge_sort_by_length(string_list)
print("Sorted strings by length (longest to shortest):")
print(sorted_strings)
