#!/usr/bin/python

import threading

def main():
    threads = []    
    for i in range(50):
        t = threading.Thread(target=greeting, args=(i+1,))
        threads.append(t)
        t.start()
    for t in threads:
        t.join()

def greeting(num):
    print("Hello from Thread " +str(num)+"!")

if __name__=="__main__":
        main()
