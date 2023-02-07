import threading
import time
import random



event = threading.Event()


def print_text():
    print("Starting the testing : ")
    event.wait()
    print("The correct test was found !!!")


t1 = threading.Thread(target=print_text)
t1.start()
for i in range(1, 11):
    time.sleep(2)
    print("test #{}".format(i))
    if i == random.randint(1, 10):
        event.set()
        break
t1.join()
