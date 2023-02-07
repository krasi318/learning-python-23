import threading


def greetings():
    for i in range(5):
        print("Hello world")


t1 = threading.Thread(target=greetings)

t1.start()
print("random text")
t1.join()
print("another text")


