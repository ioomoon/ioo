class Rectangle:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def get_area(self):
        return self.a * self.b


class Square:
    def __init__(self, a):
        self.a = a

    def get_area_square(self):
        return self.a ** 2
# возведение в степень **2 (в квадрат)


class Circle:
    def __init__(self, r):
        self.r = r

    def get_area_circle(self):
        return 3.14 * self.r **2


rect_1 = Rectangle(3, 4)
rect_2 = Rectangle(12, 5)
square_1 = Square(5)
square_2 = Square(10)
circle_1 = Circle(2)
circle_2 = Circle(5)


figures = [rect_1, rect_2, square_1, square_2, circle_1, circle_2]


for figure in figures:
    if isinstance(figure, Square):
        print(figure.get_area_square())
    elif isinstance(figure, Circle):
        print(figure.get_area_circle())
    else:
        print(figure.get_area())
