class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        array = [];
        kvp = {
            1 : 'I',
            4 : 'IV',
            5 : 'V',
            9 : 'IX',
            10 : 'X',
            40 : 'XL',
            50 : 'L',
            90 : 'XC',
            100 : 'C',
            400 : 'CD',
            500 : 'D',
            900 : 'CM',
            1000 : 'M'
        };
        if num in kvp:
           return kvp[num];
        else:
            sum = '';
            array = list(kvp.keys());
            array.sort();
            for i in range(len(array)-1 , -1, -1):
                while array[i] <= num:
                    sum += kvp[array[i]];
                    num -= array[i];
                    
            
        return sum