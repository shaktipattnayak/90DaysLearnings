

# def total_occurance_of_char():
#     char_ount = {}
#     string = input("Enter a String: ")
#     # char = input("Enter a character to find its occurance: ")
#     # count = 0
#     for i in string.lower():
#         if i in char_ount:
#             char_ount[i] += 1
#         else:
#             char_ount[i] = 1
#     # print(f"Total occurrence of '{char}' in '{string}' is: {count}")
#     print(char_ount)
# str1= "programming"
# total = {i: str1.count(i) for i in str1}

# print(total)
# # total_occurance_of_char("Prasanna", "n")

cars = ["BMW", "Audi", "BMW","Mercedes","Mercedes", "Mercedes", "Audi","BMW", "Audi","Mercedes", "Toyota", "Honda"]

total= {}
for car in cars:
    if car in total:
        total[car] += 1
    else:
        total[car] = 1
print(total)


# Remove all the zeros from a list

list_with_zeros = [0, 1, 2, 0, 3, 4, 0, 5]
def remove_zeros(lst):
    return [x for x in lst if x != 0]
print(remove_zeros(list_with_zeros))    # Alternative way to remove zeros using filter

#  Move all the zeros and ones to the end of the list
def move_zeros_ones_to_end(lst):
    zeros = [x for x in lst if x==0]
    ones = [x for x in lst if x == 1]
    others = [x for x in lst if x not in (0, 1)]
    return others +zeros + ones
print(move_zeros_ones_to_end(list_with_zeros))

# Find missing number in a list
missing_list = [1, 2, 3, 5, 6, 7, 8]
def find_missing_number(lst):
    n = len(lst) + 1  # The length of the complete list should be one more than the current list
    total_sum = n * (n + 1) // 2  # Sum of first n natural numbers
    current_sum = sum(lst)  # Sum of the current list
    return total_sum - current_sum  # The difference is the missing number
print(find_missing_number(missing_list))

# find out pair with given sum in a list 
# explaination:
# The function `find_pairs_with_sum` takes an array and a target sum as input.
# It initializes an empty list `pairs` to store the pairs that sum to the target and a set `seen` to keep track of numbers we've encountered.
# It iterates through each number in the array, calculates its complement (the number needed to reach the target sum), and checks if that complement has already been seen.
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
def find_pairs_with_sum(arr, target_sum):
    pairs = []
    seen = set()
    for num in arr:
        complement = target_sum - num
        if complement in seen:
            pairs.append((complement, num))
        seen.add(num)
    return pairs
print(find_pairs_with_sum(arr, 10))  # Example usage, looking for pairs that sum to 10

# Map, Filter, and Reduce
# Find the evens numbers for a given list using filter
def get_even_nums(n):
    if n % 2 == 0:
        return n
even_numbers = list(filter(lambda x:x % 2 == 0, arr))
print(even_numbers)

# Double the numbers in a list using map

def double_num(n):
    return n * n

double_numbers = list(map(lambda x:x*x, list(filter(lambda x:x % 2 == 0, arr))))
print(double_numbers)

# count sum of even numbers in a list using reduce
from functools import reduce
def sum(x, y):
    return x + y
sum_even_numbers = reduce(lambda x,y:x+y, list(map(lambda x: x*x, list(filter(lambda x:x % 2 == 0, arr)))))
print(sum_even_numbers)

# find the missing number from a list of numbers

unsorted_list = [5, 4, 2, 1, 7]
complete_list = [i for i in range(min(unsorted_list), max(unsorted_list) +1, 1)]
print("complete_list", complete_list)
missing_nums_list = set(complete_list) - set(unsorted_list)
print("missing_nums_list", missing_nums_list)

sorted_list = sorted(unsorted_list)
max_num = max(sorted_list)
min_num = min(sorted_list)
missing_numbers = [num for num in range(min_num, max_num + 1) if num not in sorted_list]

print("sorted_list", sorted_list)
print("missing_numbers", missing_numbers)

# find out pair with given sum value of a list suppose number is 10 the how many pairs are there in a list which sums to 10
def two_sum_pairs(arr, target_sum):
    pair = []
    seen = set()
    for num in arr:
        complement = target_sum - num
        if complement in seen:
            pair.append((complement, num))
        seen.add(num)

#Function to print full pyramid pattern
"""
pyramid pattern star
    *
   * *
  * * *
 * * * *
"""
def print_full_pyramid(n):
    for i in range(n):
        # Print leading spaces
        print(' ' * (n - i - 1), end='')
        # Print stars
        print('* ' * (i + 1))
print_full_pyramid(5)

print("\n")

def print_inverted_full_pyramid(n):
    for i in range(n, 0, -1):
        # Print leading spaces
        print(' ' * (n - i), end='')
        # Print stars
        print('* ' * i)
print_inverted_full_pyramid(5)
# if __name__ == "__main__":
    # Example usage
    # total_occurance_of_char()
    # total_occurance_of_char("Prasanna", "n")
    # total_occurance_of_char("Python Programming", "g")
    # total_occurance_of_char("Data Science", "a")
    # total_occurance_of_char("OpenAI ChatGPT", "t")