#coding=utf-8
'''
代理模式(Proxy Pattern):为其他对象提供一种代理以控制对这个对象的访问

模型:
#公共接口类
class InterFace:
    def request(self):
        pass
#真实类
class RealSubject(InterFace):
    def request(self):
        print 'RealSubject request'
#代理类 调用真实类的内部方法
class ProxySubject(InterFace)
    def request(self):
        self.real = RealSubject()
        self.real.request()
'''
class SendGift(object):
    def flower(self):
        pass

    def pursue(self):
        pass

    def skirt(self):
        pass

class Target(object):
    def __init__(self, name):
        self.name = name

class Pursuit(SendGift):
    def __init__(self, target):
        self.target = target

    def flower(self):
        print self.target.name, 'send flower'

    def pursue(self):
        print self.target.name, 'send pursue'

    def skirt(self):
        print self.target.name, 'send skirt'

class Proxy(SendGift):
    def __init__(self, Gril):
        self.poxy = Pursuit(Gril)
    def flower(self):
        self.poxy.flower()

    def pursue(self):
        self.poxy.pursue()

    def skirt(self):
        self.poxy.skirt()

if __name__ == '__main__':
    t = Target('shasha')
    P = Proxy(t)
    P.flower()