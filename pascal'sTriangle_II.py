class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        result = [[1]]
        for i in range(0,rowIndex):
            temp = [0]+ result[-1] + [0];
            row =[];
            for j in range(len(result[-1])+1):
                row.append(temp[j] + temp[j+1]);
            result.append(row)
        return result[-1]
