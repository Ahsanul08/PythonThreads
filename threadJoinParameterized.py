__author__ = 'ahsanul'


import logging, threading, time


logging.basicConfig(level=logging.DEBUG,
                    format='[%(levelname)s] (%(threadName)-10s) %(message)s'
                    )
def Daemon():
    logging.debug("starting")
    time.sleep(5)
    logging.debug("exiting")


def nonDaemon():
    logging.debug("starting")
    time.sleep(2)
    logging.debug("exiting")


d = threading.Thread(name='Daemon', target=Daemon)
d.setDaemon(True)
nd = threading.Thread(name='NonDaemon', target=nonDaemon)

d.start()
nd.start()

d.join(3)
print d.isAlive()
nd.join()
