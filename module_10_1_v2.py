# Домашнее задание по теме "Введение в потоки".
# Задача "Потоковая запись в файлы".

import threading
from time import sleep
from datetime import datetime, timedelta


def write_words(word_count, file_name):
    with open(file_name, 'w', encoding='utf-8') as f:  # Указываем кодировку UTF-8
        for i in range(1, word_count + 1):
            f.write(f"Какое-то слово № {i}\n")
            sleep(0.1)  # Задержка 0.1 сек

    print(f"Завершилась запись в файл {file_name}")


# Функция для измерения времени выполнения
def measure_time(func, *args):
    start_time = datetime.now()
    func(*args)
    end_time = datetime.now()
    return end_time - start_time


# Запуск функции с заранее определенными параметрами
timing_results = []
timing_results.append(measure_time(write_words, 10, "example1.txt"))
timing_results.append(measure_time(write_words, 30, "example2.txt"))
timing_results.append(measure_time(write_words, 200, "example3.txt"))
timing_results.append(measure_time(write_words, 100, "example4.txt"))

# Создание потоков
threads = []
thread_args = [
    (10, "example5.txt"),
    (30, "example6.txt"),
    (200, "example7.txt"),
    (100, "example8.txt")
]

# Запуск потоков для записи в файлы
for args in thread_args:
    t = threading.Thread(target=write_words, args=args)
    threads.append(t)
    t.start()

# Ожидание завершения всех потоков
for t in threads:
    t.join()

# Вывод результатов времени выполнения
total_time = sum(timing_results, timedelta())
print(f'Общее время выполнения: {total_time}')
