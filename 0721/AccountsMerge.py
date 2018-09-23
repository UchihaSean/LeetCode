class Solution(object):
    def union(self, x, y):
        fa_x = self.get_father(x)
        fa_y = self.get_father(y)
        self.father[fa_x] = fa_y

    def get_father(self, x):
        if self.father[x] == x: return x
        self.father[x] = self.get_father(self.father[x])
        return self.father[x]

    def accountsMerge(self, accounts):
        """
        :type accounts: List[List[str]]
        :rtype: List[List[str]]
        """
        self.father = {}
        emailToName = {}
        for account in accounts:
            name, emails = account[0], account[1:]
            emailToName[emails[0]] = name
            for email in emails:
                if email not in self.father:
                    self.father[email] = emails[0]
                else:
                    self.union(email, emails[0])

        group = {}
        ans = []
        for item in self.father:
            fa = self.get_father(item)
            if fa not in group:
                group[fa] = [emailToName[fa], item]
            else:
                group[fa].append(item)

        return [[group[item][0]] + sorted(group[item][1:]) for item in group]

