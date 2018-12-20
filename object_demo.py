import logging

logging.basicConfig(level=logging.INFO)


class Progarmmer:
    hobby = 'Just in coding.....'
    hobby2 = 'eat food'

    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.__weight = weight
        # logging.info(dir())

    # 没有使用类方法装饰器，必须实例化才能调用
    def get_hobby2(self):
        return self.hobby2

    # 类方法：不用实例化的时候可以调用
    @classmethod
    def get_hobby(cls):
        return cls.hobby

    # 属性 装饰器 可以在对象中调用是不加括号返回值，否则返回地址
    @property
    def get_weight(self):
        return self.__weight

    # 重载magic  add方法
    def __add__(self, other):
        if isinstance(other, Progarmmer):
            self.age = self.age + other.age
        else:
            raise Exception('The type of object must be Programmer')

    def myfavovite(self):
        return 'My favorite language is Javascript.'

# 继承
class BackendProgrammer(Progarmmer):

    def __init__(self, name, age, weight, height):
        super(BackendProgrammer, self).__init__(name, age, weight)
        self.height = height

    # 多态
    def myfavovite(self):
        return 'My favorite language is python'







if __name__ == '__main__':
    logging.info("a")

    logging.info(Progarmmer.get_hobby())
    programmer = Progarmmer('chengfei', 39, 69.4)

    logging.info(programmer.name)
    logging.info(programmer.get_weight)
    logging.info(programmer.__dict__)
    logging.info(programmer.myfavovite())
    logging.info(dir(programmer))

    backendProgrammer = BackendProgrammer('chengfei', 39, 69.4, 178)
    logging.info(backendProgrammer.get_weight)
    logging.info(backendProgrammer.height)
    logging.info(backendProgrammer.get_weight)
    logging.info(backendProgrammer.myfavovite())
    logging.info(backendProgrammer.__class__)
    logging.info(backendProgrammer + programmer)
    logging.info(backendProgrammer.age)


