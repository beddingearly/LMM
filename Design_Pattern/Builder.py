#coding=utf-8
'''
建造者模式
建造者模式(Builder):将一个复杂对象的构建与它的表示分离,使得同样的构建过程可以常见不同的表示
特性: 指挥者(Director) 指挥 建造者(Builder) 建造 Product
'''

import abc

class Builder():
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def buildArm(self):
        pass

    @abc.abstractmethod
    def buildLeg(self):
        pass

    # @abc.abstractmethod
    # def buildCook(self):
    #     pass

class Human(object):
    pass

class Thin(Builder):
    def buildArm(self):
        print 'Thin Arm'

    def buildLeg(self):
        print "Thin Leg"

    def buildHead(self):
        print 'Thin Head'


class Fat(Builder):
    def buildArm(self):
        print 'Fat Arm'

    def buildLeg(self):
        print "Fat Leg"

class Director(object):
    def __init__(self, persion):
        self.persion = persion

    def creatArm(self):
        self.persion.buildArm()

    def createLeg(self):
        self.persion.buildLeg()

if __name__ == '__main__':
    t = Thin()
    f = Fat()
    d = Director(t)
    d.creatArm()