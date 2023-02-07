import threading
import time

sema = threading.BoundedSemaphore(value=3)

 
def access(t_num):
    print("{} is trying to get access !".format(t_num))
    sema.acquire()
    print("{} is given access !".format(t_num))
    time.sleep(10)
    print("{} is releasing !".format(t_num))
    sema.release()


for t_numa in range(1, 11):
    thread1 = threading.Thread(target=access, args=(t_numa,))
    thread1.start()
    time.sleep(1)

