# Домашнее задание по теме "Потоки на классах".
# Задача "За честь и отвагу!"

import threading
import time

class Knight(threading.Thread):
    def __init__(self, name, power):
        threading.Thread.__init__(self)
        self.name = name
        self.power = power
        self.enemies = 100  # Начальное количество врагов
        self.days = 0  # Счетчик дней

    def run(self):
        print(f'{self.name}, на нас напали!')
        while self.enemies > 0:
            time.sleep(1)  # Задержка в 1 секунду, имитирующая день сражения.
            self.days += 1
            self.enemies -= self.power
            if self.enemies < 0:  # Если врагов меньше 0, устанавливаем на 0.
                self.enemies = 0
            day_word = (
                'день' if self.days % 10 == 1 and self.days % 100 != 11 else
                'дня' if self.days % 10 in [2, 3, 4] and self.days % 100 not in [12, 13, 14] else
                'дней'
            )
            print(f'{self.name} сражается {self.days} {day_word}..., осталось {self.enemies} воинов.')

        # После победы
        print(f'{self.name} одержал победу спустя {self.days} {day_word}!')


# Создание двух объектов рыцарей
first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight('Sir Galahad', 20)

# Запуск потоков
first_knight.start()
second_knight.start()

# Ожидание завершения обоих потоков
first_knight.join()
second_knight.join()

# Вывод строк об окончании сражений
print('Все битвы закончились!')