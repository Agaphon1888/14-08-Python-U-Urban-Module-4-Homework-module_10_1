# Домашнее задание по теме "Блокировки и обработка ошибок".
# Задача "Банковские операции".


import threading
import random
import time


class Bank:
    def __init__(self):
        self.balance = 1000  # Начальный баланс
        self.lock = threading.Lock()  # Блокировка для безопасного доступа к балансу

    def deposit(self):
        for _ in range(100):
            amount = random.randint(50, 500)  # Случайная сумма для внесения

            with self.lock:  # Используем блокировку для безопасного доступа к балансу
                self.balance += amount  # Увеличиваем баланс
                print(f'Пополнение: {amount}. Баланс: {self.balance}')
            time.sleep(random.uniform(0.1, 0.5))  # Задержка во времени для имитации работы

    def take(self):
        for _ in range(100):
            amount = random.randint(50, 500)  # Случайная сумма для снятия

            with self.lock:  # Используем блокировку для безопасного доступа к балансу
                if self.balance >= amount:  # Проверяем, достаточно ли средств
                    self.balance -= amount  # Уменьшаем баланс
                    print(f'Снятие: {amount}. Баланс: {self.balance}')
                else:
                    print(f'Запрос отклонён, недостаточно средств.')

            time.sleep(random.uniform(0.1, 0.5))  # Задержка во времени для имитации работы


def main():
    bank = Bank()  # Создаем экземпляр банка

    # Создаем потоки для внесения и снятия средств
    deposit_thread = threading.Thread(target=bank.deposit)
    take_thread = threading.Thread(target=bank.take)

    # Запускаем потоки
    deposit_thread.start()
    take_thread.start()

    # Дожидаемся завершения потоков
    deposit_thread.join()
    take_thread.join()

    print(f'Итоговый баланс: {bank.balance}')


if __name__ == "__main__":
    main()  # Запускаем главный цикл
