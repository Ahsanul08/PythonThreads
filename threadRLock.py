__author__ = 'ahsanul'



import threading

lock = threading.Lock()

print 'First try :', lock.acquire()
print 'Second try:', lock.acquire(0)


lock = threading.RLock()

print 'First try :', lock.acquire()
print 'Second try:', lock.acquire(0)