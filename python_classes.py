"""
PYTHON CLASSES: A TEACHING GUIDE
===============================

A class is a blueprint for creating objects. An object is one particular
instance made from that blueprint. For example, Student is a class, while
each individual student is an object.

Run this file to see the examples:
    python python_classes.py

The examples are intentionally kept in one file so they can be taught in
order. Read the explanation above each example, then run the file and inspect
the output.
"""

from abc import ABC, abstractmethod


# ---------------------------------------------------------------------------
# 1. A class, objects, attributes, and methods
# ---------------------------------------------------------------------------

class Student:
    """Represent one student and the marks they earned."""

    # A class attribute belongs to the class and is shared by its instances.
    school_name = "Python Learning Center"

    def __init__(self, name, marks):
        """Initialize each new Student object.

        __init__ is called automatically when we create an object.
        self refers to the particular object being initialized.
        """
        self.name = name       # Instance attribute: this student's name
        self.marks = marks     # Instance attribute: this student's marks

    def introduce(self):
        """An instance method uses or describes one particular object."""
        print(f"My name is {self.name}. I earned {self.marks} marks.")

    def has_passed(self):
        """Return True if this student's marks are at least 40."""
        return self.marks >= 40

    @classmethod
    def from_percentage(cls, name, percentage):
        """A class method can be used as an alternate object constructor.

        cls refers to the class (Student here), in the same way that self
        refers to one object in an instance method.
        """
        return cls(name, percentage)

    @staticmethod
    def passing_mark():
        """A static method is related to the class but needs no self or cls."""
        return 40


# ---------------------------------------------------------------------------
# 2. Creating and using objects
# ---------------------------------------------------------------------------

def teach_objects_and_methods():
    print("\n1. OBJECTS, ATTRIBUTES, AND METHODS")

    first_student = Student("Asha", 85)
    second_student = Student("Ravi", 35)

    # Dot notation reads an object's attributes and calls its methods.
    print("First student's name:", first_student.name)
    first_student.introduce()
    print("Did Asha pass?", first_student.has_passed())
    print("Did Ravi pass?", second_student.has_passed())

    # Each object has its own instance attributes.
    print("First student's marks:", first_student.marks)
    print("Second student's marks:", second_student.marks)

    # The class attribute is available through the class or an object.
    print("School:", Student.school_name)
    print("School through an object:", first_student.school_name)

    # The class attribute is shared until an instance shadows it with its own.
    first_student.school_name = "Asha's New School"
    print("Asha's school:", first_student.school_name)
    print("Ravi's school:", second_student.school_name)
    print("Class default school:", Student.school_name)

    # A class method uses cls, and a static method needs neither self nor cls.
    third_student = Student.from_percentage("Meera", 92)
    print("Created with a class method:", third_student.name)
    print("Passing mark:", Student.passing_mark())

    # Built-ins can tell us what kind of object we have.
    print("Object's type:", type(first_student).__name__)
    print("Is this a Student?", isinstance(first_student, Student))


# ---------------------------------------------------------------------------
# 3. Encapsulation and properties
# ---------------------------------------------------------------------------

class BankAccount:
    """A small example of protecting and validating an object's data."""

    def __init__(self, owner, opening_balance=0):
        self.owner = owner
        self._balance = 0
        self.deposit(opening_balance)

    @property
    def balance(self):
        """A property lets us read balance like an attribute."""
        return self._balance

    def deposit(self, amount):
        """Add a positive amount to the account."""
        if amount <= 0:
            raise ValueError("Deposit amount must be greater than zero.")
        self._balance += amount

    def withdraw(self, amount):
        """Withdraw an amount only when it is positive and affordable."""
        if amount <= 0:
            raise ValueError("Withdrawal amount must be greater than zero.")
        if amount > self._balance:
            raise ValueError("There is not enough money in the account.")
        self._balance -= amount


class Product:
    """A property setter validates a value whenever it is assigned."""

    def __init__(self, name, price):
        self.name = name
        self.price = price

    @property
    def price(self):
        """Getter: product.price returns the internally stored price."""
        return self._price

    @price.setter
    def price(self, value):
        """Setter: product.price = value checks the value before storing it."""
        if value < 0:
            raise ValueError("Price cannot be negative.")
        self._price = value


def teach_encapsulation():
    print("\n2. ENCAPSULATION AND PROPERTIES")

    account = BankAccount("Asha", 100)
    account.deposit(50)
    account.withdraw(20)
    print(f"{account.owner}'s account balance: {account.balance}")

    book = Product("Python Basics", 25)
    print(f"{book.name} costs ${book.price}.")
    book.price = 30
    print("Updated price:", book.price)

    # By convention, a leading underscore (for example _balance) means
    # "internal use". It is not strict access control. Properties provide a
    # public interface where validation or other logic can be added.
    #
    # A double leading underscore triggers name mangling; it discourages
    # accidental access but is not a security feature.


# ---------------------------------------------------------------------------
# 4. Inheritance, overriding, and polymorphism
# ---------------------------------------------------------------------------

class Person:
    """A parent/base class with behavior shared by people."""

    def __init__(self, name):
        self.name = name

    def describe_role(self):
        return f"{self.name} is a person."


class Teacher(Person):
    """A child/derived class inherits from Person and adds a subject."""

    def __init__(self, name, subject):
        # super() calls the parent class's initializer.
        super().__init__(name)
        self.subject = subject

    def describe_role(self):
        # This method overrides the parent method with more specific behavior.
        return f"{self.name} teaches {self.subject}."


class ClassroomAssistant(Person):
    """Another child class demonstrates a different implementation."""

    def describe_role(self):
        return f"{self.name} helps students in the classroom."


def teach_inheritance_and_polymorphism():
    print("\n3. INHERITANCE AND POLYMORPHISM")

    teacher = Teacher("Mr. Lee", "Python")
    assistant = ClassroomAssistant("Sam")

    print(teacher.describe_role())
    print(assistant.describe_role())
    print("Is the teacher a Teacher?", isinstance(teacher, Teacher))
    print("Is the teacher also a Person?", isinstance(teacher, Person))

    # Polymorphism: the same method call works on different object types,
    # and each object supplies its own behavior.
    people = [teacher, assistant, Person("Jordan")]
    for person in people:
        print(person.describe_role())


# ---------------------------------------------------------------------------
# 5. Composition: building an object from other objects
# ---------------------------------------------------------------------------

class Engine:
    """A component that can be used by another class."""

    def start(self):
        return "Engine started"


class Car:
    """A Car has an Engine: this relationship is called composition."""

    def __init__(self, model):
        self.model = model
        self.engine = Engine()

    def start(self):
        return f"{self.model}: {self.engine.start()}"


def teach_composition():
    print("\n4. COMPOSITION")
    car = Car("Electric Example")
    print(car.start())
    print("The car has an Engine object:", isinstance(car.engine, Engine))


# ---------------------------------------------------------------------------
# 6. Special (dunder) methods and operator behavior
# ---------------------------------------------------------------------------

class Book:
    """A book with readable text and a useful length."""

    def __init__(self, title, pages):
        self.title = title
        self.pages = pages

    def __str__(self):
        """Controls the friendly text shown by print(book) and str(book)."""
        return f"{self.title} ({self.pages} pages)"

    def __len__(self):
        """Makes len(book) return the number of pages."""
        return self.pages


def teach_special_methods():
    print("\n5. SPECIAL METHODS")
    book = Book("Learning Python", 250)
    print(book)
    print("Page count from len(book):", len(book))


# ---------------------------------------------------------------------------
# 7. Abstraction: define a common interface for child classes
# ---------------------------------------------------------------------------

class Shape(ABC):
    """An abstract base class describes behavior subclasses must provide."""

    @abstractmethod
    def area(self):
        """Every concrete shape must implement area()."""
        raise NotImplementedError


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


def teach_abstraction():
    print("\n6. ABSTRACTION")
    rectangle = Rectangle(5, 3)
    print("Rectangle area:", rectangle.area())
    # Shape() itself cannot be created because it has an abstract method.
    # A concrete child class such as Rectangle must implement area().


# ---------------------------------------------------------------------------
# 8. A simple checklist and practice ideas
# ---------------------------------------------------------------------------

def class_checklist():
    print("\nCLASS CHECKLIST")
    print("- Class: blueprint; object: instance made from the blueprint.")
    print("- __init__: initializes an object; self: the current object.")
    print("- Attribute: data stored on a class or object.")
    print("- Method: function defined inside a class.")
    print("- Inheritance: a child class reuses or specializes a parent class.")
    print("- Composition: an object contains or uses other objects.")
    print("- Encapsulation: keep data and the operations on it together.")
    print("- Polymorphism: a common operation can behave differently by object.")
    print("- Abstraction: specify required behavior without its full details.")

    print("\nPRACTICE")
    print("1. Add an email attribute to Student and display it in introduce().")
    print("2. Add a method that returns a student's letter grade.")
    print("3. Create a SavingsAccount that inherits from BankAccount.")
    print("4. Create a Circle class that inherits from Shape and implements area().")
    print("5. Add a __str__ method to Student for a friendly print(student).")


def main():
    """Run each lesson section in teaching order."""
    teach_objects_and_methods()
    teach_encapsulation()
    teach_inheritance_and_polymorphism()
    teach_composition()
    teach_special_methods()
    teach_abstraction()
    class_checklist()


if __name__ == "__main__":
    main()
