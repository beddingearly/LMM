# coding=utf-8
import math
import numpy as np
from numpy import *

class PricingFramework(object):
    def __init__(self):
        self.max_step =100
        self.k = 0
        self.greedy = 0.0001
        self.emsilon = 0.0001
        self.alpha = 0.01
       # self.sigma = 1
        self.N = 100
        self.X=[100][101]
        for xi in self.X:
            xi = np.random.randint(0,100,size = 101)
        # sum(map(sum, X)) = self.c
        self.C = 100



    def B(self,i):
        for i in range(1, self.N):
            self.B_i = (1/100)*i
        return self.B_i
    def D(self,i):
        for i in range(1, self.N):
            self.D_i = (1/100)*i
        return self.D_i
    def E(self,i):
        for i in range(1, self.N):
            self.E_i = (1/100)*i
        return self.E_i
    def x(self): #判断所有元素之和是否等于c
        for j in range(0,100):
            for i in range(0,99):
                sum += self.X[i][j]
        return (sum == self.C)
    def norm(self,i): #范数  i代表函数
        return sqrt(sum(power(i,2)))

    def pricingframework(self,i,k,t):
        k = 0
        self.Xk_t = np.zeros((100, 100,100))
        self.Xk_t[-1] = self.optimize(self.X)
        self.Lmbda = np.zeros((100,100))
        self.Lmbda[-1] = self.l(self,i,t)
        Xstar = np.zeros(100)
        Cstar = np.zeros(100)
        while (self.norm(((self.L(self.Xk_t[k], self.Lmbda[k])) - (self.L(self.Xk_t[k - 1], self.Lmbda[k - 1]))))) > self.greedy:
            t = 0
            while (self.norm((self.L(self.Xk_t[k][t+1]),self.Lmbda[k][t+1]))) - (self.L(self.Xk_t[k][t], self.Lmbda[k][t])) > self.emsilon:
                i=1
                for i in range(1,100):
                    self.Xk_t[k][t][i] = (self.lagrangian(self.Xi,self.Lmbda[k][t]) + self.individual(self.Xi).index(min(self.lagrangian(self.Xi, self.Lambda[k][t]) + self.individual(self.Xi))))
                    self.Lmbda[k][t + 1] = self.Lmbda[k][t] + self.alpha * (self.total(self,k,t,i) - self.C)
                    t += 1

            self.Xk_t[k] = self.Xk_t[k][t]
            self.Lmbda[k] = self.Lmbda[k][t]
            self.cita=np.zeros((100,100))
            for i in range(1,100):
                self.cita[k+1][i]= self.v(self.Xi).deriv(m = 1)
            k += 1
        Xstar[i] = self.Xk_t[k][t][i]
        Cstar[i] = self.cita[k][i]
        return Xstar,Cstar
    '''    def g(self,i):#信道
        self.g = random.randint(1,13)
        return self.g   '''

    '''    def B(self,i,sigma):
        return self.norm(self.g(i) / (power(self.sigma,2))  '''

    '''    def x(self, x):
        return x ** -1 '''




    def individual(self,i,k):
        if k==0:
            return self.v(i)
        else:
            return self.v(i) - self.cita[k][i] * self.Xi

    def lagrangian(self,i):
        return self.u(i) - self.Lmbda * self.Xi

    def L(self,i):
        for i in range(1,self.N):
            sum += self.lagrangian(i)
        return sum + self.Lmbda * self.C

    def u(self,i):
        return self.D(i) * self.Xi - self.E(i) * (power(self.Xi,2))

    @staticmethod
    def U(self, x,i): #控制器目的函数
        for i in range(1,self.N):
            sum += self.u(i)
            return sum

    @staticmethod
    def v(self,i): #agent目的函数
        return log(1+self.B(i) * self.Xi)

    def total(self, k, t,i):
        for i in range(1, self.N):
            sum += self.Xk_t[k][t][i]
        return sum

#    def gradient(self, x):
 #       return x

    def incentive(self,x,i,k):
        return self.lagrangian() + self.individual()

    def optimize(self,X): #问题2最优解
        T=[100]
        if self.x() == 1:
            for xi in X:
                t = xi[0]
                h = self.v(t)
                for x in xi:
                    hi=self.v(x)
                    if hi<h:
                        t=x
                        T.append(t)
            return T
        if self.x() == 0:
            pass




    def l(self,t,i):#求lambda -1
        t = 0
        xt = np.zeros((100,100))
        lmbda = np.zeros()
        while (self.norm((self.L(xt[t + 1], lmbda[t + 1]))) - (self.L(xt[t], lmbda[t]))) > self.emsilon:
            i = 1
            for i in range(1, 100):
                xt[t][i] = (self.lagrangian(self.Xi, lmbda[t]) + self.individual(self.Xi).index(min(self.lagrangian(self.Xi, self.Lambda[t]) + self.individual(self.Xi))))
                lmbda[t + 1] = lmbda[t] + self.alpha * (self.total() - self.C)
                t += 1

        Lmbda = lmbda[t]

        return Lmbda

if __name__ == '__main__':
    PricingFramework.pricingframework()




