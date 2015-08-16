__author__ = 'ahsanul'

import threading,time, logging

logging.basicConfig(level=logging.DEBUG, format='(%(threadName)-10s) %(message)s',)


def delayed():
    logging.debug(" running")
    return

t1 = threading.Timer(3, delayed)
t1.setName("t1")
t2 = threading.Timer(3,delayed)
t2.setName("t2")

logging.debug("starting timers")
t1.start()
t2.start()

logging.debug("Waiting to cancel %s",t1.getName())
time.sleep(2)
logging.debug("Time to cancel %s",t1.getName())
t2.cancel()
logging.debug("done")