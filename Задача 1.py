import math


class InvalidTriangleError(Exception):
    """Исключение, возникающее при нарушении неравенства треугольника."""
    pass


class Triangle:
    """
    Класс, представляющий геометрический треугольник.
    Стороны являются скрытыми (защищенными) переменными.
    """

    def __init__(self, a: float, b: float, c: float):
        # Проверка на положительность сторон
        if a <= 0 or b <= 0 or c <= 0:
            raise InvalidTriangleError("Стороны треугольника должны быть положительными числами.")

        # Теорема о соотношении сторон (Неравенство треугольника)
        # Сумма любых двух сторон должна быть строго больше третьей
        if a + b <= c or a + c <= b or b + c <= a:
            raise InvalidTriangleError(f"Треугольник со сторонами {a}, {b}, {c} не существует!")

        self._a = a
        self._b = b
        self._c = c

    @property
    def a(self) -> float:
        return self._a

    @property
    def b(self) -> float:
        return self._b

    @property
    def c(self) -> float:
        return self._c

    @property
    def perimeter(self) -> float:
        """Вычисление периметра."""
        return self._a + self._b + self._c

    @property
    def area(self) -> float:
        """Вычисление площади по теореме Герона."""
        p = self.perimeter / 2  # Полупериметр
        return math.sqrt(p * (p - self._a) * (p - self._b) * (p - self._c))

    def get_angles(self) -> tuple:
        """Вычисление углов треугольника по теореме косинусов (в градусах)."""

        # Теорема косинусов: cos(A) = (b^2 + c^2 - a^2) / (2*b*c)
        def acos(val):
            return math.acos(max(-1.0, min(1.0, val)))

        angle_a = math.degrees(acos((self._b ** 2 + self._c ** 2 - self._a ** 2) / (2 * self._b * self._c)))
        angle_b = math.degrees(acos((self._a ** 2 + self._c ** 2 - self._b ** 2) / (2 * self._a * self._c)))
        angle_c = 180.0 - angle_a - angle_b

        return round(angle_a, 2), round(angle_b, 2), round(angle_c, 2)

    def __str__(self):
        return f"Треугольник со сторонами ({self._a}, {self._b}, {self._c})"


    #ПРОВЕРКА



def main():

    t = Triangle(3, 4, 5)
    print(t)
    print(f"Периметр: {t.perimeter}")
    print(f"Площадь: {t.area}")
    print(f"Углы: {t.get_angles()}")
    print("-" * 30)

if __name__ == "__main__":
    main()