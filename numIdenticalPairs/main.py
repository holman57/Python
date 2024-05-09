from typing import List


class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        n = len(nums)
        t = 0
        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] == nums[j]:
                    t += 1
        return t


solution = Solution()
print(solution.numIdenticalPairs([1, 2, 3, 1, 1, 3]), 4)
print(solution.numIdenticalPairs([1, 1, 1, 1]), 6)
print(solution.numIdenticalPairs([1, 2, 3]), 0)
