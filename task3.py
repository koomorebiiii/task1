import math
from abc import ABC, abstractmethod
from typing import Self

class Shape(ABC):
# Абстрактный базовый класс для геометрических фигур
    
    @abstractmethod
    def area(self) -> float:
        pass
    
    @abstractmethod
    def perimeter(self) -> float:
        pass
    
    def area_greater_than(self, other: Self) -> bool:
        return self.area() > other.area()
    
    def perimeter_greater_than(self, other: Self) -> bool:
        return self.perimeter() > other.perimeter()


class Rectangle(Shape):
    def __init__(self, width: float, height: float) -> None:
        self._validate_positive(width, height)
        self._width = width
        self._height = height
    
    def _validate_positive(self, *values: float) -> None:
        if any(v <= 0 for v in values):
            raise ValueError("Размеры должны быть положительными")
    
    def area(self) -> float:
        return self._width * self._height
    
    def perimeter(self) -> float:
        return 2 * (self._width + self._height)
    
    def __str__(self) -> str:
        return f"Rectangle({self._width}x{self._height})"


class Square(Rectangle):
    def __init__(self, side: float) -> None:
        super().__init__(side, side)
    
    def __str__(self) -> str:
        return f"Square({self._width})"


class Triangle(Shape):
    def __init__(self, a: float, b: float, c: float) -> None:
        self._validate_triangle(a, b, c)
        self._sides = (a, b, c)
    
    def _validate_triangle(self, a: float, b: float, c: float) -> None:
        if any(side <= 0 for side in (a, b, c)):
            raise ValueError("Стороны должны быть положительными")
        if (a + b <= c) or (a + c <= b) or (b + c <= a):
            raise ValueError("Невалидный треугольник")
    
    def area(self) -> float:
        p = self.perimeter() / 2
        return math.sqrt(p * (p - self._sides[0]) * (p - self._sides[1]) * (p - self._sides[2]))
    
    def perimeter(self) -> float:
        return sum(self._sides)
    
    def __str__(self) -> str:
        return f"Triangle{self._sides}"


class Circle(Shape):
    def __init__(self, radius: float) -> None:
        if radius <= 0:
            raise ValueError("Радиус должен быть положительным")
        self._radius = radius
    
    def area(self) -> float:
        return math.pi * self._radius ** 2
    
    def perimeter(self) -> float:
        return 2 * math.pi * self._radius
    
    def __str__(self) -> str:
        return f"Circle(r={self._radius})"


def compare_values(val1: float, val2: float, equal_str: str) -> str:
    if val1 > val2:
        return "больше"
    elif val1 < val2:
        return "меньше"
    else:
        return equal_str


def compare_shapes(shape1: Shape, shape2: Shape) -> None:
    area1, area2 = shape1.area(), shape2.area()
    perimeter1, perimeter2 = shape1.perimeter(), shape2.perimeter()
    
    area_comparison = compare_values(area1, area2, "равна")
    perimeter_comparison = compare_values(perimeter1, perimeter2, "равен")
    
    print(f"{shape1} vs {shape2}:")
    print(f"  Площадь: {area_comparison} ({area1:.1f} vs {area2:.1f})")
    print(f"  Периметр: {perimeter_comparison} ({perimeter1:.1f} vs {perimeter2:.1f})")


def main():
    # Создание фигур
    shapes = [
        Square(5),
        Rectangle(4, 6),
        Triangle(3, 4, 5),
        Circle(3)
    ]
    
    # Вывод информации
    print(" ХАРАКТЕРИСТИКИ ФИГУР ")
    for shape in shapes:
        print(f"{shape}: площадь={shape.area():.1f}, периметр={shape.perimeter():.1f}")
    
    print("\n СРАВНЕНИЕ ФИГУР ")
    for i in range(len(shapes)):
        for j in range(i + 1, len(shapes)):
            compare_shapes(shapes[i], shapes[j])
            print()


if __name__ == "__main__":
    main()