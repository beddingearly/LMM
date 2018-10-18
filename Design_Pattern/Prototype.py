#coding=utf-8
'''
原型模式

用原型实例指定创建对象的种类,并且通过拷贝这些原型创建新的对象
原型模式是用场景:需要大量的基于某个基础原型进行微量修改而得到新原型时使用
'''
# 原型抽象类
class Prototype(object):

    def clone(self):
        pass

    def deep_clone(self):
        pass

# 工作经历类
class WorkExperience(object):

    def __init__(self):
        self.timearea = ''
        self.company = ''

    def set_workexperience(self,timearea, company):
        self.timearea = timearea
        self.company = company


# 简历类
class Resume(Prototype):

    def __init__(self,name):
        self.name = name
        self.workexperience = WorkExperience()

    def set_personinfo(self,sex,age):
        self.sex = sex
        self.age = age
        pass

    def set_workexperience(self,timearea, company):
        self.workexperience.set_workexperience(timearea, company)

    def display(self):
        print self.name
        print self.sex, self.age
        print '工作经历',self.workexperience.timearea, self.workexperience.company

    def clone(self):
        pass
        #return copy(self)

    def deep_clone(self):
        pass
        #return deepcopy(self)


def fun1(s=''):
    if len(s) <= 1:
        return [s]
    sl = []
    for i in range(len(s)):
        for j in fun1(s[0:i] + s[i + 1:]):
            sl.append(s[i] + j)
    return sl


class Solution:
    def IsPopOrder(self, pushV, popV):
        # write code here
        if len(pushV) != len(popV):
            return False
        j = 0
        i = 1
        s = [pushV[0]]
        while len(s) != 0:
            print j
            if i < 5 and j < 5:
                if pushV[i] == popV[j]:
                    i += 1
                    j += 1
                elif pushV[i] != popV[j]:
                    s.append(pushV[i])
                    i += 1
            elif len(s) != 0 and s[-1] == popV[j]:
                s.pop()
                j += 1
            else:
                return False
        return True


if __name__ == '__main__':
    a = Solution()
    print a.IsPopOrder([1,2,3,4,5], [4,3,5,1,2])

