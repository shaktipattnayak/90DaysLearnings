class Singleton:
    _instance = None
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

s1 = Singleton()
s2 = Singleton()
print(s1 is s2)  # True, both variables point to the same instance
print(id(s1), id(s2))  # Both IDs will be the same, indicating they are the same instance