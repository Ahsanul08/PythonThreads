__author__ = 'ahsanul'

import threading
import logging

logging.basicConfig(level=logging.DEBUG,
                    format='(%(threadName)-10s) %(message)s',
                    )

class myOwnThread(threading.Thread):
    def run(self):
        logging.debug("running")
        return

for i in range(5):
    t = myOwnThread()
    t.start()
