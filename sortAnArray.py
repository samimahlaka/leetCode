class Solution(object):
    def sortArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        if len(nums) <= 1:
            return nums;
        
        else:

            leftarray = nums[0:len(nums)//2];
            rightarray = nums[len(nums)//2:];

            self.sortArray(leftarray);
            self.sortArray(rightarray);

            i=0;
            j=0;
            k=0;

            while i < len(leftarray) and j < len(rightarray):
                if leftarray[i] < rightarray[j]:
                    nums[k] = leftarray[i];
                    i+=1;
                else:
                    nums[k] = rightarray[j];
                    j+=1;
                k+=1;

            while i < len(leftarray):
                nums[k]= leftarray[i];
                i+=1;
                k+= 1;

            while j < len(rightarray):
                nums[k] = rightarray[j];
                j+=1;
                k+= 1;

            return nums   

        
            