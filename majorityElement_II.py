class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        length = math.floor(len(nums)/3);
        kvp={};
        temp =[];
        for i in nums:
            if i in kvp:
                kvp[i] = kvp[i] + 1;
            else:
                kvp[i] = 1;

        for i in kvp.keys():
            if kvp[i] > length:
                temp.append(i);
        return temp;