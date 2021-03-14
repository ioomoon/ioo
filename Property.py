class Square:
    def __init__(self, a):
        self.a = a

    @property
    def get_area_square(self):
        return self.a ** 2
# возведение в степень **2 (в квадрат)

    @get_area_square.setter
    def get_area_square(self, value):
        if value > 0:
            self.value = value
        else:
            raise ValueError("Значение должно быть положительным")


square1 = Square(4)
print(square1.get_area_square)
square1.get_area_square = 5
print(square1.get_area_square)