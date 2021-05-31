# Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
# Атрибут реализовать как приватный.
# В рамках метода реализовать переключение светофора в режимы: красный, желтый, зеленый.
# Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды, третьего (зеленый) — на ваше усмотрение.
# Переключение между режимами должно осуществляться только в указанном порядке (красный, желтый, зеленый).
# Проверить работу примера, создав экземпляр и вызвав описанный метод.
# Задачу можно усложнить, реализовав проверку порядка режимов, и при его нарушении выводить соответствующее сообщение и завершать скрипт.

import time
import random

class TrafficLight:
    __colour = ['Red', 'Yellow', 'Green']


    def running(self):
        ConditionList = [[0, 1, 2], [1, 2, 0], [2, 0, 1], [9, 9, 0], [9, 9, 1], [9, 9, 2], [9, 0, 1], [9, 1, 2], [9, 2, 0], [9, 9, 9]] # Перечислены возможные последовательности цветов
        CurrentList = [9, 9, 9] # список показывающий последние три цвета. Изначально заполнен заглушками.
        while True:
            if CurrentList not in ConditionList:
                print('Traffic light is broken!')
                break
            else:
                i = random.choice(range(0, 2))
                CurrentList.append(i)
                CurrentList.pop(0)
                if i == 0:
                    print(f'Current colour is >>> {TrafficLight.__colour[i]}')
                    time.sleep(7)
                elif i == 1:
                    print(f'Current colour is >>> {TrafficLight.__colour[i]}')
                    time.sleep(2)
                elif i == 2:
                    print(f'Current colour is >>> {TrafficLight.__colour[i]}')
                    time.sleep(6)

MainStreet = TrafficLight()
MainStreet.running()
