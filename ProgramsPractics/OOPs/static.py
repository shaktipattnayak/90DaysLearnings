class Utils:
    @staticmethod
    def convert_camel_case(string):
        return ' '.join(word.capitalize() for word in string.split())
    
x = Utils.convert_camel_case("hello world")  # Output: HelloWorld
print(type(x))  # Output: <class 'str'>