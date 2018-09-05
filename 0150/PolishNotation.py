class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """

        list = []

        for char in tokens:
            if char not in "+-*/":
                list.append(char)
            else:
                y = int(list.pop())
                x = int(list.pop())
                if char == "+": x = x + y
                if char == "-": x = x - y
                if char == "*": x = x * y
                if char == "/":
                    if x<0 and y<0:
                        x = x/y
                    else:
                        if  x<0 or y<0:
                            x = -(abs(x) / abs(y))
                        else:
                            x = x/y
                list.append(x)

        return int(list[0])


test = Solution()
print test.evalRPN(["4","13","5","/","+"])
