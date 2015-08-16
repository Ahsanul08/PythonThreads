__author__ = 'ahsanul'

import threading,logging

logging.basicConfig(level=logging.DEBUG, format= '(%(threadName)-10s)  %(message)s')

class threadWithArgs(threading.Thread):
    def __init__(self, group = None, target = None, name= None, args =(),kwargs=None, verbose = None):
        threading.Thread.__init__(self,group= group, name= name, target= target, verbose= verbose)
        self.args = args
        self.kwargs = kwargs
        return

    def run(self):
        logging.debug("Thread started with argument ", self.args, " and keyword argument ", self.kwargs )

for i in range(5):
    t = threadWithArgs(args=(i,),kwargs={"a":"A", "b":"B"})
    t.start()
