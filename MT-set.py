'''
useing multi threading 
my result is faster
'''
import time
from threading import Thread

first = time.perf_counter()
def show(name):
    print(f"process {name} is start")
    time.sleep(3)
    print(f"process {name} is finished")

t1 = Thread(target=show,args=('Thread1',))
t2 = Thread(target=show,args=('Thread2',))
 
t1.start()
t2.start()

t1.join()
t2.join()

second = time.perf_counter()

print( second - first)
print('proses end')
