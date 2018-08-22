from multiprocessing import Process, Pipe
import time
import os

# 创建管道对象
child_conn, parent_conn = Pipe()


# 创建一个子进程函数
def fun(name):
    time.sleep(2)
    child_conn.send('hello'+str(name))
    print(os.getppid(), '-----', os.getpid())


jobs = []
for i in range(5):
    p = Process(target = fun, args = (i,))
    jobs.append(p)
    p.start()

for i in range(5):
    data = parent_conn.recv()
    print(data)

for i in jobs:
    i.join()
