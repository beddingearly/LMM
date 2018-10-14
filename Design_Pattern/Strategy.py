#coding=utf-8
'''
策略模式
1. 与建造者模式大致类似，构造一个策略抽象类Strategy，定义抽象方法
2. 构造具体策略StrategyA，继承策略抽象类
3. 构造Context类，实例化具体类，作为参数传入Context
'''
import abc
class Strategy(object):
    __metaclass__ = abc.ABCMeta
    @abc.abstractmethod
    def do(self):
        pass

class StrategyA(Strategy):

    def do(self):
        print 'A'

class StrategyB(Strategy):

    def do(self):
        print "B"

class context(object):

    def __init__(self, strategy):
        self.strategy = strategy

    def do_strategy(self):
        self.strategy.do()

if __name__ == '__main__':
    s = StrategyA()
    c = context(s)
    c.do_strategy()