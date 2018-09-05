class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        if num1=="0" or num2 =="0": return "0"
        list = [0 for i in range(len(num1)+len(num2))]
        for i in range(len(num1)):
            for j in range(len(num2)):
                x, y = len(num1)-1-i, len(num2)-1-j
                num_x, num_y = int(num1[x]), int(num2[y])
                list[i+j] += num_x*num_y
        for i in range(len(list)-1):
            list[i+1]+= list[i] / 10
            list[i] = list[i] % 10
        list.reverse()
        multiply_string = ""
        j = 0
        while list[j] == 0: j+=1
        for i in range(j,len(list)):
            multiply_string+=str(list[i])
        return multiply_string




test = Solution()
print test.multiply("123","456")