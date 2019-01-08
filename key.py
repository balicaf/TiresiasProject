import Queue
import keyboard
import string
import time
from threading import *


# I can't find a complete list of keyboard keys, so this will have to do:
keys = list(string.printable[0:36])
## keyboard don't support complexe carractere

def listen(key,q):
    while True:
        keyboard.wait(key)
        a = key
        print "listen : ",a
        q.put(a)
    print "exit loop"
    q.put(None)

def startKeyboard():
    threads = [Thread(target=listen, kwargs={"key":key,"q":queue}) for key in keys]
    for thread in threads:
        thread.start()

queue = Queue.Queue()
threads = [Thread(target=listen, kwargs={"key":key,"q":queue}) for key in keys]
startKeyboard()



#for thread in threads:
#    thread.start()
#threads.start()
