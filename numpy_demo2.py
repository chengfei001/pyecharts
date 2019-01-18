import numpy as np
import logging

logging.basicConfig(level=logging.INFO)


x = np.arange(16)
logging.info(x)
logging.info(x[3:9])
logging.info(x[3:9:2])


ind = [3, 5, 10]
logging.info(x[ind])
