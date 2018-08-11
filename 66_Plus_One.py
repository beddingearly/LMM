class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        s = ''
        for i in digits:
            s += str(i)
        return [int(i) for i in list(str(int(s)+1))]

