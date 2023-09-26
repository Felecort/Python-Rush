
class Name:
    def __get__(self, obj, objtype=None):
        if obj:
            return obj.__name.capitalize()
    
    def __set__(self, obj, name):
        obj.__name = name.lower()


class Dog:
    __colors = ["unset", "black", "white", "mixed"]
    name = Name()

    def __init__(self, name, color, breed):
        self.name = name
        self.color = color
        self.__breed = breed

    def get_breed(self):
        return self.__breed
    
    def set_color(self, color):
        try:
            color = Dog.__colors.index(color)
        except ValueError:
            if isinstance(color, int) and 0 <= color <= len(Dog.__colors) - 1:
                pass
            color = 0
        self.__color = color

    def get_color(self):
        return Dog.__colors[self.__color]
    
    def delete_color(self):
        self.__color = 0

    breed = property(get_breed)
    color = property(get_color, set_color, delete_color, "Color for the Dog class")


bobik = Dog("bobik", "color", "wss")
bobik.name = "KESHA"
print(bobik.name)


