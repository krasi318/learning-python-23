import threading
import time


event = threading.Event()


def func():
    print("Starting a new game: \n")
    # events waits to be triggered / the thread is paused but still running and waiting
    event.wait()
    print("New world created !!!\n")


t1 = threading.Thread(target=func)
t1.start()
time.sleep(5)

x = input("Press 'y' to continue : ")
if x == "y":
    print("Creating world...")
    time.sleep(10)
    # triggers the event
    event.set()
