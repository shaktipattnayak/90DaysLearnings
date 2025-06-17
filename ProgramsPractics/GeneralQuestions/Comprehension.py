# List comprehension is a concise way to create lists in Python.
#  It allows you to generate a new list by applying an expression to each item in an existing iterable 
# (like a list, tuple, or string) and optionally filtering items based on a condition. The syntax for list comprehension is as follows:

# Lisr of squares of the numbers from 1 to 10
squrea = [i**2 for i in range(1, 11)]
print(squrea)

# List of even numbers from 1 to 20
evens = [i for i in range(1, 21) if i % 2 == 0]
print(evens)

# List of uppercase letters from a given string
string = "hello world"
uppercase_letters = [char.upper() for char in string if char.isalpha()]
print(uppercase_letters)

# List of lengths of each word in a sentence
sentence = "List comprehensions are powerful"
word_lengths = [len(word) for word in sentence.split()]
print(word_lengths)

# List of numbers divisible by both 3 and 5 from 1 to 50
divisible_by_3_and_5 = [i for i in range(1, 51) if i % 3 == 0 and i % 5 == 0]
print(divisible_by_3_and_5)

# Flatten a 2D list into a 1D list
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened = [num for row in matrix for num in row]
print(flattened)

# Reverse each word in a sentence using list comprehension
sentence = "List comprehensions are powerful"
reversed_words = [word[::-1] for word in sentence.split()]
print(reversed_words)

# Reverse each word in a sentence using list comprehension but only if the word length is greater than 3 if less than 3 then keep the word as it is.
sentence = "Hi List comprehensions are powerful"
reversed_words = [word[::-1] if len(word) > 3 else word for word in sentence.split()]
print(reversed_words)

# # Reverse each word in a sentence using list comprehension but without using slice or any in build function to reverse the word.
# sentence = "Hi List comprehensions are powerful"
# reversed_words = [''.join(word[i] for i in range(len(word) - 1, -1, -1)) for word in sentence.split()]
# print(reversed_words)

# Reverse each word in a sentence without using list comprehension and slice or any in build function to reverse the word.
sentence = "What a beautiul day, I am happy to be here"
reversed_words = []
for word in sentence.split():
    reversed_word = ''
    for i in range(len(word) - 1, -1, -1):
        reversed_word += word[i]
    reversed_words.append(reversed_word)
print(reversed_words)





# reversed_words = [''.join(reversed(word)) for word in sentence.split()]