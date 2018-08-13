class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        la = len(a)
        lb = len(b)
        index = 0
        s = ''
        if la > lb:
            b = '0'*(la-lb) + b
        else:
            a = '0'*(lb-la) + a
        a = a[::-1]
        b = b[::-1]
        for i in range(len(a)):
            if index == 0:
                if a[i] == '1' and b[i] == '1':
                    s += '0'
                    index = 1
                elif a[i] == '0' and b[i] == '0':
                    s += '0'
                    index = 0
                else:
                    s += '1'
                    index = 0
            else:  #index == 1
                if a[i] == '1' and b[i] == '1':
                    s += '1'
                    index = 1
                elif a[i] == '0' and b[i] == '0':
                    s += '1'
                    index = 0
                else:
                    s += '0'
                    index = 1
        if index == 1:
            s += '1'
        return s[::-1]

if __name__ == '__main__':
    a = "11"
    b = "1"
    c = Solution()
    print c.addBinary(a, b)