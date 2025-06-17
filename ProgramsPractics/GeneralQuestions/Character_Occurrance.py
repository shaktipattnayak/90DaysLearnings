# Find the total occurrence of a character in a string
def char_occurrence(string, char):
    count = 0
    for i in string:
        if i == char:
            count +=1
    return count
print(f"Total occurrence of 'o' in 'hello world' is: {char_occurrence("hello world", "o")}")

# Find the total occurrence of each character in a string.
def each_char_occurrence(string):
    char_count = {}
    for char in string:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count
print(each_char_occurrence("hello world"))

# Find the total occurrence of a character in a string using dictionary comprehension.
# def char_occurrence_dict_comp(string, char):
#     return {char:string.count(char) for char in string}
# print(char_occurrence_dict_comp("hello world", "o"))
def each_char_occurrence_dict_comp(string):
    return {i:string.count(i) for i in string}

print(each_char_occurrence_dict_comp("hello world"))

# def reverse_string(string):
#     return string[::-1]
# print(reverse_string("hello world"))

def reverse_each_word_of_string(string):
    for word in string.split():
        if word[0].lower() in ["a", "e", "i", "o", "u"]:
            string = string.replace(word, word[::-1])
        # else:
        #     string = string.replace(word, word[::-1])
    return string
# print(reverse_string("hello world"))
print(reverse_each_word_of_string("Hello India"))