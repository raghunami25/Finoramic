# Problem Link - https://www.interviewbit.com/problems/3-sum/
# Solution for 3Sum problem
class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def threeSumClosest(self, A, B):
        A.sort()
        diff = None
        for i in range(len(A) - 2):
            j = i+1
            k = len(A)-1
            while k > j:
                sumOfNo = A[i] + A[j] + A[k]
                if sumOfNo == B:
                    return sumOfNo
                if diff is None or abs(B - sumOfNo) < abs(B - diff):
                    diff = sumOfNo
                if sumOfNo < B:
                    j += 1
                else:
                    k -= 1
        return diff

