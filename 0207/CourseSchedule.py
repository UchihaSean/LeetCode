class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        du = [0 for _ in range(numCourses)]
        for i, j in prerequisites:
            du[i] += 1
        q = []
        for i in range(len(du)):
            if du[i] == 0:
                q.append(i)
        l = -1
        while l + 1 < len(q):
            l += 1
            now = q[l]
            for i, j in prerequisites:
                if j == now:
                    du[i] -= 1
                    if du[i] == 0:
                        q.append(i)
        flag = True
        for t in du:
            if t != 0: flag = False
        return flag


