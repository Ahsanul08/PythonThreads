__author__ = 'ahsanul'

import logging
import threading
import time

logging.basicConfig(level=logging.DEBUG,
                    format='(%(threadName)-10s) %(message)s',
                    )

def waitForEvent(e):
    logging.debug("Waits until event is set")
    event_set = e.wait()
    logging.debug("Event set: %s ", event_set)


def waitForEventTimeout(e,timeout):
    while not e.isSet():
        logging.debug("Wait for a time to set event")
        event_set = e.wait(1)
        logging.debug("Event set: %s", event_set)
        if event_set:
            logging.debug("processing the event")
        else:
            logging.debug("Doing other work")



e = threading.Event()

t1 = threading.Thread(target = waitForEvent, name= "blocking", args=(e,)  )
t2 = threading.Thread(target=waitForEventTimeout, name="non-blocking", args=(e,2))

t1.start()
t2.start()

logging.debug("Waiting before setting the event")
time.sleep(3)
e.set()
logging.debug("event is set")

