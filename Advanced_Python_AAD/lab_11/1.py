import threading
import random
import time
import sys


def thread_job():
    global counter
    old_counter = counter
    time.sleep(random.randint(0, 1))
    counter = old_counter + 1
    print('{} '.format(counter), end='')
    sys.stdout.flush()


counter = 0
threads = [threading.Thread(target=thread_job) for _ in range(10)]
for thread in threads:
    thread.start()
for thread in threads:
    thread.join()
print(counter)

#Это происходит потому что когда потоки (thread_job()) запускаются они берут себе, то значение counter, которое есть на момент запуска. Аналогично в процессе работы они изменяют counter каждый в своё время. Из-за того, что последним может закончить не 10 - counter может и не принять нужное значение.