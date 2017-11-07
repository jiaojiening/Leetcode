class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        ls=[]
        for i in range(0, len(nums)):
            item = target - nums[i]
            nums[i] = "done"
            if item in nums:
                ls.append(i)
                ls.append(nums.index(item))
        return ls
