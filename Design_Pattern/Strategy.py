#coding=utf-8
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