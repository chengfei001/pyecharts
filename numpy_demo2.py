import numpy as np
import logging
import  array

logging.basicConfig(level=logging.INFO)


x = np.arange(16)
logging.info(x)
logging.info(x[3:9])
logging.info(x[3:9:2])


ind = [3, 5, 10]
logging.info(x[ind])
logging.info(np.__version__)

arr = array.array('i', [i for i in range(10)])
logging.info(arr[5])
arr[5] = 100
logging.info(arr[5])
logging.info(arr)


nparr = np.array([i for i in range(10)])
logging.info(nparr)
logging.info(nparr.dtype)
nparr[5] = 8.3
logging.info(nparr)

nparr2 = np.array([1,2,3.5])
logging.info(nparr2.dtype)


logging.info(np.zeros(10))
logging.info(np.zeros(10).dtype)
logging.info(np.zeros(100,dtype=int))


logging.info(np.zeros(shape=(3, 5), dtype=int))
logging.info(np.ones(shape=(3, 2), dtype=int))

logging.info(np.full(shape=(3, 3), fill_value=999))

logging.info(np.arange(0, 1, 0.1))


# linspace
logging.info(np.linspace(0, 20, 7, dtype=int))

# random
logging.info(np.random.randint(0, 10, size=(10, 2)))

# 种子
# np.random.seed(100)
logging.info(np.random.randint(0, 10, size=(10, 2)))

# np.random.seed(100)
logging.info(np.random.randint(0, 10, size=(10, 2)))

logging.info(np.random.random(10))
logging.info(np.random.random((3, 2)))

logging.info(np.random.normal())
logging.info(np.random.normal(10, 100))
logging.info(help(np.random))


x = np.arange(30)

X = x.reshape(3, -1)
logging.info(X)
logging.info(X.ndim)
logging.info(X.shape)
logging.info(x[:5:2])
logging.info(x[::-1])
logging.info(X[:2, :3])
logging.info(X[:2, ::2])
# 只取第一列
logging.info(X[:, 0])
X[0, 0] = 100
logging.info(X)
logging.info(x)


y = np.array([1, 2, 3])
z = np.array([3, 2, 1])


'''合并'''
logging.info(np.concatenate([y, z]))

A = np.array([[11, 12, 13], [14, 15, 16]])
logging.info(np.concatenate([A, A]))
logging.info(x.reshape(3, -1))
logging.info(np.concatenate([A, x.reshape(-1, 3)]))

logging.info(np.vstack([A, y]))


B = np.full((2, 2), 100)
logging.info(np.hstack([A, B]))

''' numpy 分割'''
x = np.arange(16).reshape(4, 4)
logging.info(x)

x1, x2 =  np.vsplit(x, [1])
logging.info(x1)
logging.info(x2)

y1, y2 = np.hsplit(x,[-1])

logging.info(y1)
logging.info(y2)

