class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        d = {}
        for i in range(len(numbers)):
            if numbers[i] in d.keys():
                return [d[numbers[i]] + 1, i + 1]
            d[target - numbers[i]] = i