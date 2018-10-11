#coding=utf-8
'''
一天学一种设计模式
https://blog.csdn.net/zheng_lan_fang/article/details/76550093
https://www.cnblogs.com/onepiece-andy/p/python_factory_method_pattern.html

抽象工厂

先创建工厂接口IFactory方法-->再创建各个具体工厂去创建各个实例

'''
import abc
class Human(object):
    def done(self):
        print 'ML'
    def swap(self):
        print 'paws'

class Leifeng(Human):
    def __init__(self):
        self.a = 'b'
    def swap(self):
        print 'swap'

    def wash(self):
        print 'wash'

    def cook(self):
        print 'cook'

class graducte(Leifeng):
    def __init__(self):
        super(Leifeng, self).swap()
        super(graducte, self).swap()

class ungraducte(Leifeng):
    pass

class IFactory(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def create(self):#method
        pass

class graduateFactory(IFactory):
    def create(self):
        return graducte()

class ungraducateFactory(IFactory):
    def create(self):
        return ungraducte()


if __name__ == '__main__':
    factory = graduateFactory()
    factory.create()
    # graduate = a.buildGraduateFactory().do()