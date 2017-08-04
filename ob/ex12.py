# -*- coding:utf-8 -*-
from multiprocessing import Pool, TimeoutError
import time
# pool.map   process(无法控制进程数量)   pool.apply_async

def f(x):
    print x*x
    time.sleep(1)
    return x*x


pool = Pool(processes=4)              # start 4 worker processes
res_list = []
for i in range(10):
  res = pool.apply_async(f, [i,])  # 即res = Process(target=f, args=[i,])
  print '----:', i
  res_list.append(res)

for r in res_list:
    print r.get(timeout=0.3)

print '-----------'
print pool.map(f, range(10))
