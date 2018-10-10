#coding=utf-8
'''
一天学一种设计模式
https://blog.csdn.net/zheng_lan_fang/article/details/76550093

工厂模式
定义一个用于创建对象的接口，让子类决定实例化哪一个类。
Factory Method 使一个类的实例化延迟到其子类。

先创建工厂接口IFactory-->再创建各个具体工厂去创建各个实例

'''
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
    def buildGraduateFactory(self):
        return graduateFactory()
    def buiildUngraduateFactory(self):
        return ungraducateFactory()

class graduateFactory(IFactory):
    def do(self):
        return graducte()

class ungraducateFactory(IFactory):
    def do(self):
        return ungraducte()


if __name__ == '__main__':
    a = IFactory()
    graduate = a.buildGraduateFactory().do()

