class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        size = len(nums)
        sums = [(i, j)
                for i in range(size)
                for j in range(i, size)
                if i != j and (nums[i] + nums[j]) == target]
        return sums[0]

    def twoSum_caching(self, nums, target):
        seen = {}
        for i, v in enumerate(nums):
            remaining = target - v
            if remaining in seen:
                return [seen[remaining], i]
            seen[v] = i
        return []
    