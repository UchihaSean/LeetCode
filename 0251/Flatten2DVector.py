class Vector2D(object):

    def __init__(self, vec2d):
        """
        Initialize your data structure here.
        :type vec2d: List[List[int]]
        """
        self.index = -1
        self.vec = []
        for v in vec2d:
            for s in v:
                self.vec.append(s)

    def next(self):
        """
        :rtype: int
        """
        self.index += 1
        return self.vec[self.index]

    def hasNext(self):
        """
        :rtype: bool
        """
        if self.index + 1 < len(self.vec): return True
        return False

# Your Vector2D object will be instantiated and called as such:
# i, v = Vector2D(vec2d), []
# while i.hasNext(): v.append(i.next())