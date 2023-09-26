


class Dog:
    def __init__(self, name: str, color: str, breed: str) -> None:
        # Implicitly call set_name
        self.name = name.lower()
        self.color = color
        self.__breed = breed

    def get_name(self):
        print("name Getter called")
        return self.__name.capitalize()
    
    def set_name(self, name: str):
        print("name Setter called")
        self.__name = name.lower()

    def get_breed(self):
        return self.__breed

    # getter, setter
    breed = property(get_breed)
    name = property(get_name, set_name)


dog = Dog("bob", "white", "Buldog")
print(dog.breed)
# dog.breed = "bulba"
