# Домашнее задание по теме "Очереди для обмена данными между потоками."
# Задача "Потоки гостей в кафе."

import threading
import time
import random
from queue import Queue

class Table:
    def __init__(self, number):
        self.number = number
        self.guest = None  # Гость за столом, изначально None

class Guest(threading.Thread):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):
        # Гость находится за столом от 3 до 10 секунд
        time.sleep(random.randint(3, 10))

class Cafe:
    def __init__(self, *tables):
        self.queue = Queue()  # Очередь для гостей
        self.tables = tables   # Список столов

    def guest_arrival(self, *guests):
        for guest in guests:
            # Пытаемся посадить гостя за стол
            assigned = False
            for table in self.tables:
                if table.guest is None:  # Если стол свободен
                    table.guest = guest    # Сажаем гостя за стол
                    guest.start()          # Запускаем поток гостя
                    print(f"{guest.name} сел(-а) за стол номер {table.number}")
                    assigned = True
                    break
            if not assigned:
                # Если не нашли свободный стол, ставим в очередь
                self.queue.put(guest)  # Добавляем в очередь
                print(f"{guest.name} в очереди")

    def discuss_guests(self):
        while not self.queue.empty() or any(table.guest is not None for table in self.tables):
            for table in self.tables:
                if table.guest is not None:
                    if not table.guest.is_alive():  # Если гость закончил приём пищи
                        print(f"{table.guest.name} покушал(-а) и ушёл(ушла)")
                        print(f"Стол номер {table.number} свободен")
                        table.guest = None  # Освобождаем стол

                        # Проверяем, есть ли очередной гость
                        if not self.queue.empty():
                            next_guest = self.queue.get()  # Берем следующего из очереди
                            table.guest = next_guest
                            next_guest.start()  # Запускаем поток нового гостя
                            print(f"{next_guest.name} вышел(-ла) из очереди и сел(-а) за стол номер {table.number}")
            time.sleep(1)  # Задержка для симуляции времени обслуживания

# Создание столов
tables = [Table(number) for number in range(1, 6)]
# Имена гостей
guests_names = [
    'Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
    'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra'
]
# Создание гостей
guests = [Guest(name) for name in guests_names]
# Заполнение кафе столами
cafe = Cafe(*tables)
# Приём гостей
cafe.guest_arrival(*guests)
# Обслуживание гостей
cafe.discuss_guests()