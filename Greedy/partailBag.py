#coding=utf-8

class Good(object):
    def __init__(self, id, weight, value):
        self.id = id
        self.weight = weight
        self.value = value
        self.vw = self.value/self.weight

class Bag(object):
    def select(self, goods):
        solution = {}
        for i in goods:
            tmp = i.value/i.weight
            solution[i.id] = tmp
        #  对单位价值进行排序
        solution_ = sorted(solution.items(), key=lambda d: d[1], reverse=True)
        full = 20
        w = 0
        v = 0
        for j in solution_:  # [(2, 1.6), (3, 1.5), (1, 1.3888888888888888)]
            for i in goods:  # [Good(1, 18.0, 25.0), Good(2, 15.0, 24.0), Good(3, 10.0, 15.0)]
                if i.id == j[0]:
                    if w == full:
                        break
                    elif i.weight > full:  # 直接溢出
                        w = full
                        v = v + j[1] * w
                    elif w + i.weight > full:  # 加上这个就溢出
                        t = full - w
                        w = full
                        v = v + j[1] * t
                    elif w + i.weight <= full:  # 未溢出
                        w += i.weight
                        v = v + j[1] * i.weight
        print v

if __name__ == '__main__':
    a = [Good(1, 18.0, 25.0), Good(2, 15.0, 24.0), Good(3, 10.0, 15.0)]
    b = Bag()
    b.select(a)