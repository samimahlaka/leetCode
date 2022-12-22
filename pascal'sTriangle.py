class Solution:
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows == 0:
            return [];
        else:
            result =[[1]];
            temp = [];
            if numRows == 1:
                return result;
            else:
                for i in range(1, numRows):
                    temp = [0] + result[-1] + [0];
                    row = [];
                    for j in range(len(result[-1])+1):
                        row.append(temp[j] + temp[j + 1]);
                    result.append(row);
                return result;