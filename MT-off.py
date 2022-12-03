'''
when dont be useing multi threading 
my result is very slower
'''
import time

first = time.perf_counter()

def show(name):
    print(f"process {name} is start")
    time.sleep(3)
    print(f"process {name} is finished")

t1 = show('Thread1')
t2 = show('Thread2')

second = time.perf_counter()

print( second - first)
print('proses end')
