# Задача "За честь и отвагу!"
import threading
import time

days_of_wars = []


class Knight(threading.Thread):
    def __init__(self, name, power):
        threading.Thread.__init__(self)
        self.name = name
        self.power = power

    def war(self, enemies=100):
        global days_of_wars
        days_of_war = 0
        while enemies > 0:
            enemies -= self.power
            time.sleep(1)
            days_of_war += 1
            print(f'{self.name} сражается {days_of_war}, осталось {enemies} воинов.')
        print(f'{self.name} одержал победу спустя {days_of_war} дней(дня)!')
        days_of_wars.append(days_of_war)

    def run(self):
        print(f'{self.name}, на нас напали!')
        self.war()


first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)
first_knight.start()
second_knight.start()
first_knight.join()
second_knight.join()
print(f'Все битвы закончились за {max(days_of_wars)} дней(дня)!')
