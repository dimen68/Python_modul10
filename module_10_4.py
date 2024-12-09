# Задача "Потоки гостей в кафе"

from queue import Queue
from random import randint
from threading import Thread
from time import sleep
from urllib.request import build_opener


class Table:
    def __init__(self, number):
        self.number = number
        self.guest = None


class Guest(Thread):
    def __init__(self, name):
        super().__init__()
        self.guest = Thread(name=name)
        self.name = name

    def run(self):
        sleep(randint(3, 9))


class Cafe:
    def __init__(self, *tables):
        self.queue = Queue()
        self.tables = []
        for i in tables:
            self.tables.append(i)

    def guest_arrival(self, *guests):
        guest_count = 0
        for k in self.tables:
            if k.guest is None:
                k.guest = guests[guest_count]
                guests[guest_count].start()
                print(f'{guests[guest_count].name} сел(-а) за стол номер {k.number}')
                guest_count += 1
        for l in range(guest_count, len(guests)):
            self.queue.put(guests[l])
            print(f'{guests[l].name} в очереди')
        print(f'{len(guests) - self.queue.qsize()} гостей рассажены и {self.queue.qsize()} поставлены в очередь')

    def discuss_guests(self):
        busy_table = 0
        for k in self.tables:
            if k.guest is not None:
                busy_table += 1
        while not self.queue.empty() or busy_table != 0:  # Если за столом есть гость(поток) и гость(поток) закончил приём пищи(поток завершил работу - метод is_alive), то вывести строки "<имя гостя за текущим столом> покушал(-а) и ушёл(ушла)" и "Стол номер <номер стола> свободен". Так же текущий стол освобождается (table.guest = None).
            for k in self.tables:
                if k.guest is not None and not k.guest.is_alive():
                    print(f'{k.guest.name} покушал(-а) и ушёл(ушла).\nСтол номер {k.number} свободен ')
                    k.guest = None
                    busy_table -= 1
                elif k.guest is None and not self.queue.empty():
                    next_guest = self.queue.get()
                    k.guest = next_guest
                    busy_table += 1
                    print(f'{next_guest.name} вышел(-ла) из очереди и сел(-а) за стол номер {k.number}')
                    k.guest.start()


if __name__ == '__main__':
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
