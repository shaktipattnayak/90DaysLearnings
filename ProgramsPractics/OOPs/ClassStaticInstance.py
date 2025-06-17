# Example of Class Method, Static Method and Instance Method in Python.
class Example:
    # Class variable
    class_variable = "This is a class variable"
    def __init__(self, instance_variable):
        # Instance variable
        self.instance_variable = instance_variable

    def instance_method(self):
        print(f"Instance variable self.instance_variable: {self.instance_variable}")
        print(f"Class variable self.class_variable: {Example.class_variable}")

    @classmethod
    def class_method(cls):
        print(f"Class variable cls.class_variable: {cls.class_variable}")

    @staticmethod
    def static_method():
        print("This is a static method")
        print(f"Class variable Example.class_variable: {Example.class_variable}")

