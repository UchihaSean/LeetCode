class Solution(object):
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        point_dict = {}
        for i in range(len(equations)):
            if equations[i][0] not in point_dict:
                point_dict[equations[i][0]] = [[equations[i][1], values[i]]]
            else:
                point_dict[equations[i][0]].append([equations[i][1], values[i]])
            if equations[i][1] not in point_dict:
                point_dict[equations[i][1]] = [[equations[i][0], 1.0 / values[i]]]
            else:
                point_dict[equations[i][1]].append([equations[i][0], 1.0 / values[i]])
        ans = []
        for x, y in queries:
            if x not in point_dict or y not in point_dict:
                ans.append(-1.0)
                continue
            visited = {}
            for item in point_dict:
                visited[item] = False
            visited[x] = True
            value = dfs(point_dict, x, y, visited)
            ans.append(value)

        return ans


def dfs(point_dict, x, y, visited):
    if x == y:
        return 1.0
    for point, value in point_dict[x]:
        if not visited[point]:
            visited[point] = True
            v = dfs(point_dict, point, y, visited)
            if v != -1.0:
                return v * value
            visited[point] = False
    return -1.0


test = Solution()

print test.calcEquation([ ["a", "b"], ["b", "c"] ], [2.0, 3.0], [ ["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"] ])
