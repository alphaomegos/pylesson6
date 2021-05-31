# Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина).
# Значения данных атрибутов должны передаваться при создании экземпляра класса.
# Атрибуты сделать защищенными.
# Определить метод расчета массы асфальта, необходимого для покрытия всего дорожного полотна.
# Использовать формулу: длина*ширина*масса асфальта для покрытия одного кв метра дороги асфальтом, толщиной в 1 см*число см толщины полотна.
# Проверить работу метода.
# Например: 20м*5000м*25кг*5см = 12500 т

class Road:
    def __init__(self, _length, _width):
        self._length = _length
        self._width = _width

class Enmasse(Road):
    def __init__(self, _length, _width, density, height):
        super().__init__(_length, _width)
        self.height = height
        self.density = density

    def MassCount(self):
        return self._length * self._width * self.density * self.height

Result = Enmasse(5000, 20, 25, 0.05)
print(f'Mass of the road with {Result.height} m height, {Result._length} m length and {Result._width} m width  is >>>  {Result.MassCount()}')
