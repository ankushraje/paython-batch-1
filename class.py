# class
# shopping_cart.add()
# shopping_cart.remove()
# shopping_cart.get_total()

# Classes come to rescue

# class is blueprint of creating object
# everyclass object is created using a blueprint of class


# class: blueprint for creating a new object
# object: instance of a class
# Class: Human
# Object: John, Mary, Jack


# create class
# Pascal Naming Convention First Letter of Every word is UpperCase no undescore


class Point:
    default_color = "red"

    def __init__(
        self, x, y
    ):  # Magic Method called by automatoically python interpreter
        self.x = x
        self.y = y
        self.tags = {}

    def __str__(self):  # Magic method
        return f"({self.x}.{self.y})"

    def __eq__(self, other):  # Magic method
        return self.x == other.x and self.y == other.y

    def __gt__(self, other):  # Magic method
        return self.x > other.x and self.y > other.y

    def __get__(self, tag):
        return self.tags.get(tag.lower(), 0)

    def draw(self):  # python by default set current pointing object
        print(f"Point({self.x},{self.y})")

    @classmethod  # decorated
    def zero(cls):  # ref to class intesfl
        return cls(0, 0)


# point = Point()
# print(type(point))

# print(isinstance(point, int))

# To Intitialize the variables of x and y
point = Point(1, 2)  # print(point.x)
point.draw()

point = Point(4, 5)  # Instance they diffrent atributes, methods and functinality
point.draw()

# human have two eyes and two legs for all humans
print(Point.default_color)
Point.default_color = "yellow"
print(point.default_color)

# class level atribute share all accross the instaces of class

# magic Methods
# point = Point.zero()
print(str(point))
point["python"]=10
first = Point(1, 2)  # print(point.x) # two dfiifrent memory location
other = Point(3, 4)  # print(point.x)
print(first == other)
print(first < other)
