import logging
logging.basicConfig(level=logging.INFO)



def dec(func):
    def in_dec(*args):
        if len(args) == 0:
            return 0
        for arg in args:
            if not isinstance(arg, int):
                logging.info(type(arg))
                raise Exception('The type of object s must be int.')
        return func(*args)
    return in_dec

@dec
def my_sum(*args):
    return sum(args)


logging.info(my_sum(1,3,9))
# my_sum = dec(my_sum)

# logging.info(my_sum(1,3,45))
# x = my_sum(1,3,45)
# logging.info(type(x))
# logging.info(x)
# logging.info(my_sum(1,3,5,8))
