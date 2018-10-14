#coding=utf-8
"""
设计模式——装饰模式
装饰模式(Decorator Pattern):动态的给一个对象添加一些额外的职责,就增加功能来说,装饰模式比生成子类更为灵活.
特点: 有效的把类的核心职责和装饰功能区分开,而且可以去除相关类中重复的装饰逻辑
装饰子类的父类的方法Decorate中，一个实例内decorate包含另一个实例
子类继承父类，构造方法也继承
"""
class Persion(object):
    def show(self):
        pass

class Finery(Persion):
    def Decorate(self, component):
        self.component = component

    def show(self):
        self.component.show()

class Skirt(Finery):
    def show(self):
        print 'skirt'
        self.component.show()


class Pants(Finery):
    def show(self):
        print 'pants'
        self.component.show()


class Blouser(Finery):
    def __init__(self):
        super(Blouser, self).__init__()
    def show(self):
        print 'blouser'
        self.component.show()

if __name__ == '__main__':
    P = Persion()

    s = Skirt()
    p = Pants()
    b = Blouser()

    s.Decorate(P)
    p.Decorate(s)
    b.Decorate(p)
    b.show()
