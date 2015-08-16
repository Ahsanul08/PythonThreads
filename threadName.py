__author__ = 'ahsanul'

import threading,time

def first():
    print threading.currentThread().getName(), "is being executed"
    time.sleep(2)
    print threading.currentThread().getName(), "is finished"

def second():
    print threading.currentThread().getName(), "is being executed"
    time.sleep(3)
    print threading.currentThread().getName(), "is finished"

one = threading.Thread(name="A_Nice_Thread", target=first)
two = threading.Thread(name= "A_jealous_thread", target = second)
three = threading.Thread(target=first)

one.start()
two.start()
three.start()