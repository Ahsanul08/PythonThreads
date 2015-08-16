__author__ = 'ahsanul'

import threading

def functionToBeInvoked():
    """This function will be executed via thread"""
    print "Invoked"
    return

threads = []

for i in range(5):
    t = threading.Thread(target=functionToBeInvoked)
    threads.append(t)
    t.start()

print threads
