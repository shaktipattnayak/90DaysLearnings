# Linear search algorithm
# Time complexity: O(n)
# Space complexity: O(1)
def linear_search(arr, target):
    for i, val in enumerate(arr):
      if val == target:
         return i
    return -1
print(linear_search([1, 2, 3, 4, 5], 2)) # Output: 2