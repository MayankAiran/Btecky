def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1

# Example usage
my_list = [1, 3, 5, 7, 9]
target_number = 5

result = binary_search(my_list, target_number)

if result != -1:
    print("Element found at index", result)
else:
    print("Element not found")
