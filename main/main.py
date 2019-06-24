'''
Created on Jun 19, 2019

@author: Brad Bosak
'''

import threading, datetime

def programstart():
    print("Program start time = ", datetime.datetime.now())

def timer1print():
    print("Timer 1: ", datetime.datetime.now())
    timer1()

def timer1():
    threading.Timer(2.0, timer1print).start()
    
def timer2print():
    print("Timer 2: ", datetime.datetime.now())
    timer2()

def timer2():
    threading.Timer(3.0, timer2print).start()

def main():
    programstart()
    timer1()
    timer2()

main()

# import threading
# import datetime
# 
# def printit():
#   threading.Timer(5.0, printit).start()
#   threading.Timer(2.0, printit).start()
#   print (datetime.datetime.now())
# 
# printit()

# import threading
# import time
# import datetime
# 
# def hello():
#     print("First timer", datetime.datetime.now())
# 
# if __name__ == '__main__':
#     print("Program start time:", datetime.datetime.now())
#     t = threading.Timer(3.0, hello)
#     t.start()

# import threading
# import time
# import logging
# import datetime
#  
# logging.basicConfig(level=logging.DEBUG,
#                     format='(%(threadName)-9s) %(message)s',)
#  
# def f():
#     logging.debug(datetime.datetime.now())
#     return
#  
# if __name__ == '__main__':
#     t1 = threading.Timer(10, f)
#     t1.setName('t1')
#     t2 = threading.Timer(3, f)
#     t2.setName('t2')
#  
#     logging.debug('starting timers...')
#     t1.start()
#     t2.start()
#  
#     logging.debug('waiting before canceling %s', t2.getName())
#     time.sleep(2)
#     logging.debug('canceling %s', t2.getName())
#     print("before cancel is t2 alive?", t2.is_alive())
#     t2.cancel()
#     time.sleep(2)
#     print("after cancel is t2 alive?",t2.is_alive())
#  
#     t1.join()
#     t2.join()
#  
#     logging.debug('done')