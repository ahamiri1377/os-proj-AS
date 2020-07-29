from multiprocessing.pool import ThreadPool
from multiprocessing import Manager
import time
import datetime


def thr_func(x,y,type, map, time, id):

    # #Child
    # if datetime.timedelta.total_seconds(datetime.datetime.today() - time) > type:
    #     map[x][y].
    #     child1 = pool.apply_async(thr_func, x, y, type, map, datetime.datetime.today())
    #
    print("thread created: " + str(id))
    time.sleep(0.1)

#  Getting the inputs

r = int(input(" Please insert r : "))
s = int(input(" Please insert s : "))
n = int(input(" Please insert n : "))
m = int(input(" Please insert m : "))
k = int(input(" Please insert k : "))
t = int(input(" Please insert t : "))

pool = ThreadPool(processes=1)

manager = Manager()

table = [[[] for j in range(m)] for i in range(n)]

print(table)
table = manager.list(table)

counter = 1

t = table[0]
for i in range(r):
    for j in range(s):
        x = pool.apply_async(thr_func, ((n // r) * (i + 1) - 1, (m // s) * (j + 1) - 1, i+1, table, datetime.datetime.today(), counter))
        counter += 1
        table[(n // r) * (i + 1) - 1][(m // s) * (j + 1) - 1].append(x)

# for i in range(n):
#     for j in range(m):
#             table = table[0]
#             print(table[j][i], end='\t')
#     print("\n", end='')


# test


