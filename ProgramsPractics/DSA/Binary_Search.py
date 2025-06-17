# Efficently search a sorted list by repeatedly dividing the search interval in half.

def binary_search(arr, target):
    sortedarr = sorted(arr)
    low, high = 0, len(sortedarr) - 1
    while low <= high:
        mid = (low + high)//2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

print(binary_search([1, 2, 3, 4, 5], 2)) # Output: 1