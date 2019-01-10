from pandas import Series, DataFrame
import pandas as pd
import logging


logging.basicConfig(level = logging.INFO)


logging.info(dir(Series))

s_from_array = Series([100, 200])
logging.info(s_from_array)

s_from_dict = Series({'2010':100, '2012':200, '2014':300})
logging.info(s_from_dict)
logging.info("数据索引:")
logging.info(s_from_array.index)
logging.info("数据值:")
logging.info(s_from_array.values)

# 各项指标，可以参照numpy
logging.info("数据类型为：")
logging.info(type(s_from_array))
logging.info('数据大小：')
logging.info(s_from_array.size)
logging.info('数据类型：')
logging.info(s_from_array.dtype)
logging.info('数据维度：')
logging.info(s_from_array.ndim)
logging.info('数据形状：')
logging.info(s_from_array.shape)
logging.info(s_from_dict.to_string())

data = pd.DataFrame({'id':[1,1,1,2,2,2],'value':['A','B','C','D','E','F']})
logging.info('values:  '+data['value']+'  xxxx')
data['value'] = data['value'].apply(lambda x:','+ x)
logging.info(data)
data1 = data.groupby(by='id').sum()
logging.info(data1)
data1['value'] = data1['value'].apply(lambda x :[x[1:]])
logging.info(data)
logging.info(data1)
