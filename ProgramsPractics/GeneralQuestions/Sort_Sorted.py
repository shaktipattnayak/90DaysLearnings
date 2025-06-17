# Difference between sorted and sort
# sorted() returns a new sorted list from the elements of any iterable.
# list.sort() sorts the list in place and returns None.
# sorted() can be used on any iterable, while list.sort() can only be used on lists.
list1 = [10, 11, 12, 3, 40, 5, 6, 9, 8, 7]

# sorted_list = sorted(list1)
# print("Sorted List:", sorted_list)
# print(f"Unsorted list {list1}")
# list1.sort()
# print(f"Sorted list using sort function {sorted(list1)}")

# Find the smallest and the second smallest element in a list
def find_smallest_and_secong_smallest_number(lst):
    if len(lst) <2:
        raise ValueError("The list must contain at least two elements.")
    smallest = float('inf')
    second_smallest = float("inf")
    for num in lst:
        if num <= smallest:
            second_smallest = smallest
            smallest = num
        elif num <= second_smallest:
            second_smallest = num
    return smallest, second_smallest
smallest, second_smallest = find_smallest_and_secong_smallest_number(list1)
print(f"Smallest number: {smallest}, Second smallest number: {second_smallest}")


# Find the largest and the second largest element in a list
def find_largest_and_second_largest_number(lst):
    if len(lst) < 2:
        raise ValueError("The list must contain at least two elements.")
    largest = float('-inf')
    second_largest = float('-inf')
    for num in lst:
        if num >= largest:
            second_largest = largest
            largest = num
        elif num >= second_largest:
            second_largest = num
    return largest, second_largest

