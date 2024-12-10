''' Задача5.Абстрактный класс
 Вы работаете в компании,занимающейся разработкой программного обеспечения
 для архитектурных проектов.Вам необходимо разработать программу для расчёта
 площади различных геометрических фигур, таких как круги, прямоугольникии
  треугольники.
 Задача
 Создайте:
 ● класс Shape, который будет базовым классом для всех фигур и будет
 хранить пустой метод area,который наследники должны переопределить;
 ● класс Circle;
 ● класс Rectangle;
 ● класс Triangle.
 Классы Circle,Rectangle и Triangle наследуют от класса Shape и реализуют метод
 для вычисления площади фигуры'''

from abc import ABC, abstractmethod
import math

class Shape(ABC):

    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return self.radius * self.radius * math.pi

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return self.base * self.height * 0.5


circle = Circle(2)
print(circle.area())

rectangle = Rectangle(2,4)
print(rectangle.area())

triangle = Triangle(5, 3)
print(triangle.area())

#shape = Shape() #TypeError: Can't instantiate abstract class Shape without an implementation for abstract method 'area'