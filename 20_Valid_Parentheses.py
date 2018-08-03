#coding=utf-8
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        for i in s:
            if i == '(' or i == '[' or i == '{':
                stack.append(i)
            elif i == ')' and len(stack)>0:
                if stack.pop() == '(':
                    continue
                else:
                    return False
            elif i == ']' and len(stack)>0:
                if stack.pop() == '[':
                    continue
                else:
                    return False
            elif i == '}' and len(stack)>0:
                if stack.pop() == '{':
                    continue
                else:
                    return False
            else:
                return False
        if len(stack) > 0:
            return False
        return True
if __name__ == '__main__':
    a = Solution()
    s = "["
    #s = '{(]}'
    print a.isValid(s)
