# OOP Inheritance Practice Questions - Python

# Question 1
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_person(self):
        print("Name:", self.name)
        print("Age:", self.age)


class Student(Person):
    def __init__(self, name, age, roll_no):
        super().__init__(name, age)
        self.roll_no = roll_no

    def display_student(self):
        print("Roll No:", self.roll_no)


# Question 2
class Vehicle:
    def __init__(self, brand):
        self.brand = brand

    def show_brand(self):
        print("Brand:", self.brand)


class Car(Vehicle):
    def __init__(self, brand, model):
        super().__init__(brand)
        self.model = model

    def show_model(self):
        print("Model:", self.model)


# Question 3
class Animal:
    def eat(self):
        print("Animal is eating")


class Dog(Animal):
    def bark(self):
        print("Dog is barking")


class Puppy(Dog):
    def weep(self):
        print("Puppy is weeping")


# Question 4
class Person1:
    def __init__(self, name):
        self.name = name


class Employee(Person1):
    def __init__(self, name, salary):
        super().__init__(name)
        self.salary = salary


class Manager(Employee):
    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = department


# Question 5
class Father:
    def bike(self):
        print("Father owns a bike")


class Mother:
    def jewellery(self):
        print("Mother owns jewellery")


class Child(Father, Mother):
    pass


# Question 6
class Teacher:
    def teach(self):
        print("Teaching students")


class Researcher:
    def research(self):
        print("Doing research")


class Professor(Teacher, Researcher):
    pass


# Question 7
class Shape:
    pass


class Circle(Shape):
    def draw(self):
        print("Drawing Circle")


class Rectangle(Shape):
    def draw(self):
        print("Drawing Rectangle")


class Triangle(Shape):
    def draw(self):
        print("Drawing Triangle")


# Question 8
class EmployeeBase:
    def work(self):
        print("Employee is working")


class Developer(EmployeeBase):
    pass


class Tester(EmployeeBase):
    pass


# Question 9
class A:
    def methodA(self):
        print("Method A")


class B(A):
    def methodB(self):
        print("Method B")


class C(A):
    def methodC(self):
        print("Method C")


class D(B, C):
    def methodD(self):
        print("Method D")


# Question 10
class Employee2:
    def employee(self):
        print("Employee Method")


class Manager2(Employee2):
    def manager(self):
        print("Manager Method")


class Developer2(Employee2):
    def developer(self):
        print("Developer Method")


class TeamLead(Manager2, Developer2):
    def teamlead(self):
        print("TeamLead Method")


# Question 11
class Person2:
    def __init__(self, name):
        self.name = name


class Student2(Person2):
    def __init__(self, name, roll_no):
        super().__init__(name)
        self.roll_no = roll_no


# Question 12
class Vehicle2:
    def __init__(self, brand):
        self.brand = brand


class Car2(Vehicle2):
    def __init__(self, brand, model, price):
        super().__init__(brand)
        self.model = model
        self.price = price


# Question 13
class Account:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance


class SavingsAccount(Account):
    def __init__(self, account_number, balance, interest_rate):
        super().__init__(account_number, balance)
        self.interest_rate = interest_rate


# Question 14
class Person3:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Teacher2(Person3):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject


# Question 15
class Product:
    def __init__(self, product_name, price):
        self.product_name = product_name
        self.price = price


class Electronics(Product):
    def __init__(self, product_name, price, warranty):
        super().__init__(product_name, price)
        self.warranty = warranty


print("OOP Inheritance Practice File Loaded Successfully")
