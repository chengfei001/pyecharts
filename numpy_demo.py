import numpy as np
import logging

logging.basicConfig(level=logging.INFO)


a = np.array([1, 2, 3])
logging.info(type(a))
logging.info(a.shape)
a = a.reshape((1,-1))
# a = a.reshape((-1,1))
logging.info(a.shape)

a = np.array([1, 2, 3, 4, 5, 6])
logging.info(a.shape)
a = a.reshape((2, -1))
logging.info(a.shape)
a[1, 1] = 55
logging.info(a)


a = np.array([1, 2, 3, 4, 5, 6])
logging.info(a.shape)
a = a.reshape((3, -1))
logging.info(a.shape)

a = np.zeros((5, 5))
logging.info(a)

a = np.full((8, 8), 100)
logging.info(a.shape)
logging.info(a)
a = np.random.random((3,8))
logging.info(a.shape)
logging.info(a)

b = np.array([[1, 2, 3, 4], [3, 4, 5, 6], [6, 7, 8, 9]])
logging.info(b.shape)
logging.info(b)

logging.info(b[1:, 1:3])
logging.info((b[1:, 1:3]).shape)
c = b[0:, 2:4]
logging.info(c.shape)
logging.info(c)
logging.info(type(c))

d = b[0:, -2:4]
logging.info('\r\n d:\r\n%s' %d)

b[0:, 1:2] += 100
logging.info(b )
logging.info(np.arange(3))
logging.info(np.arange(3, 19))

b[np.arange(3), -2:] += 5
logging.info(b.shape)
logging.info(b)

b[[0, 1, 2], [3, 3, 2]] += 100
logging.info(b)
resule_index = b >10
logging.info(resule_index)
logging.info(b[resule_index])
logging.info(b[b>10])

e = np.array([1.2, 13.4])
logging.info(e.dtype)
f = np.array(e, dtype=np.int32)
logging.info(f)
logging.info(f.dtype)
logging.info(f.data)

# 数学运算和常用函数
f = np.array([[1, 3, 45, 9], [1, 3, 4, 8]])
g = np.array([[2, 8, 8, 4], [8, 2, 4, 7]])
logging.info(f+g)

# 加和，总计
logging.info(f.sum())
logging.info(f.sum(axis=0))
logging.info(f.sum(axis=1))

# 平均
logging.info(f.mean())

# 随机数
logging.info(np.random.uniform(5, 10, 3))
logging.info(np.random.random())

# 数组重复现实的次数
logging.info(np.tile(f,(5,3)))


# 排序
logging.info(f)
logging.info(f.argsort())
# logging.info(f[f.argsort(axis=1)])


# 矩阵转置
logging.info(f.T)
logging.info(f.transpose())
h = np.array([1, 1, 1, 1])
logging.info(f+h)

