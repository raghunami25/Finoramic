# Problem Link -  https://www.interviewbit.com/problems/anagrams/
# Anagram Solution
class Solution:
    # @param A : tuple of strings
    # @return a list of list of integers
    def anagrams(self, A):
        result = {}
        for i in range(len(A)):
            key = "".join(sorted(A[i]))
            if key in result:
                result[key].append(i+1)
            else:
                result[key] = [i+1]
        
        for key in result:
            if len(result[key])<1:
                del result[key]
        return [i for i in result.values()]
