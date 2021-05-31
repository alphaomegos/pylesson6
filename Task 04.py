# Реализуйте базовый класс Car.
# У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
# Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
# Для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов.
# Выполните доступ к атрибутам, выведите результат.
# Выполните вызов методов и также покажите результат.

class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return f'{self.name} is started'

    def stop(self):
        return f'{self.name} is stopped'

    def turn_north(self):
        return f'{self.name} is turned north'

    def turn_south(self):
        return f'{self.name} is turned south'

    def turn_west(self):
        return f'{self.name} is turned west'

    def turn_east(self):
        return f'{self.name} is turned east'

    def show_speed(self):
        return f'Current speed of {self.name} is {self.speed} km/h'


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Current speed of town car {self.name} is {self.speed} km/h')
        if self.speed > 60:
            return f'{self.name} is exceeded town car speed limit!'
        else:
            return f'Speed of {self.name} is under limit for town car'


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Current speed of work car {self.name} is {self.speed}')
        if self.speed > 40:
            return f'Speed of {self.name} is exceeded work car speed limit!'
        else:
            return f'Speed of {self.name} is under limit for work car'


class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def police(self):
        if self.is_police:
            return f'{self.name} is from police department'


Ferrari = SportCar(100, 'Red', 'Ferrari', False)
Suzuki = TownCar(70, 'Blue', 'Suzuki', False)
Freightliner = WorkCar(30, 'White', 'Freight', False)
Ford = PoliceCar(200, 'Mixed', 'Ford', True)


print(f'Town is waking up! We see {Ferrari.name} {Suzuki.name} {Ford.name} {Freightliner.name}')
print(f'{Ferrari.go()}\n{Suzuki.go()}\n{Ford.go()}\n{Freightliner.go()}')
print(Ferrari.turn_north())
print(f'{Freightliner.stop()}')
print(f'Is {Freightliner.name} a police car? {Freightliner.is_police}!')
print(f'Is {Ford.name} a police car? {Ford.is_police}!')
print(Suzuki.show_speed())
print(f'What colour of {Suzuki.name}? It is {Suzuki.color}!')
print(Ford.turn_west())
print(Ford.show_speed())
print(Ford.police())