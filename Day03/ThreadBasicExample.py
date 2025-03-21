import threading
import time
from threading import Thread



def fun():
    print("function executing.....", threading.currentThread().name)
    time.sleep(2)
    print("completed executing....", threading.currentThread().name)

thrd1 = Thread(target=fun, name = "t1")
thrd2 = Thread(target=fun, name = "t2")
thrd3 = Thread(target=fun, name = "t3")

st = time.perf_counter()

thrd1.start()
thrd2.start()
thrd3.start()

thrd1.join()
thrd2.join()
thrd3.join()

et = time.perf_counter()

print(f"Total time taken :{et - st}")