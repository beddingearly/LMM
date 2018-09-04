class Solution(object):
    def fairCandySwap(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        result = []
        for i in range(len(A)):
            for j in range(len(B)):
                sum1 = 0
                sum2 = 0
                for a in A:
                    if a == A[i]:
                        continue
                    sum1 += a
                sum1 += B[j]
                for b in B:
                    if b == B[j]:
                        continue
                    sum2 += b
                sum2 += A[i]
                if sum1 == sum2:
                    result.append(A[i])
                    result.append(B[j])
                    return result
