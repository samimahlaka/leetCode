class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = list(set(nums));
        count =0;
        if len(nums) >=3 :
            nums.remove(max(nums));
            nums.remove(max(nums));
            return max(nums);
        else:
            return max(nums)
