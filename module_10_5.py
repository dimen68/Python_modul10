# Задача "Многопроцессное считывание"
import multiprocessing
import time


def read_info(name):
    all_data = []
    with open(name, 'r') as f:
        all_data.append(f.readlines())


if __name__ == '__main__':
    file_names = [f'./file {number}.txt' for number in range(1, 5)]

    start_time = time.time()
    for file in file_names:
        read_info(file)
    end_time = time.time()
    print(f'Линейное считывание: {round(end_time - start_time, 3)}')

    time.sleep(2)

    with multiprocessing.Pool(4) as pool:
        start_time = time.time()
        pool.map(read_info, file_names)
        end_time = time.time()
        print(f'Многопроцессное считывание: {round(end_time - start_time, 3)}')
