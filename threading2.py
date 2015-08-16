__author__ = 'ahsanul'

import threading

def calledFunction(i):
    print "Thread no.", i+1 , " executed"
    return


for i in range(5):
    t = threading.Thread(target=calledFunction, args =(i,))
    t.start()


