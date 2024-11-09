# Домашнее задание по теме "Многопроцессное программирование".
# Задача "Многопроцессное считывание".

import time
import multiprocessing

def read_info(name):
    all_data = []
    with open(name, 'r') as f:
        while True:
            line = f.readline()
            if not line:  # Если строка пустая, выходим из цикла
                break
            all_data.append(line.strip())  # Убираем символы новой строки и добавляем в список
    # Вернуть или вывести данные не требуется, поэтому просто завершаем выполнение функции

if __name__ == '__main__':
    # Создаем список названий файлов
    filenames = [f'./file {number}.txt' for number in range(1, 5)]

    # Линейный вызов
    # start_time = time.time()
    # for filename in filenames:
    #     read_info(filename)
    # linear_time = time.time() - start_time
    # print(f'{linear_time:.6f} (линейный)')

    # Многопроцессный вызов
    start_time = time.time()
    with multiprocessing.Pool() as pool:
        pool.map(read_info, filenames)
    multiprocessing_time = time.time() - start_time
    print(f'{multiprocessing_time:.6f} (многопроцессный)')