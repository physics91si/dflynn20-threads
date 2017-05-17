import random
import time
import threading


class Num():
    def __init__(self,counter=0):
        self.counter = counter
        self.lock = threading.Lock()
    def increment(self):
        with self.lock:
            temp = self.counter
            temp += 1
            self.counter = temp
        
def worker(num):
    num.increment()
    return

threads = []
num = Num()
for i in range(15):
    t = threading.Thread(target=worker, args=(num,))
    threads.append(t)
    myName = "Thread " + str(i)        
    t.setName(myName)
    t.start()

for t in threads:
    t.join()
    print(t.getName(), "joined")
print(num.counter)
