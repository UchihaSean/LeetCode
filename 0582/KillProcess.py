class Solution(object):
    def get_father(self, t, fa):
        if t not in fa or fa[t] == 0: return 0
        if fa[t] == t: return t
        fa[t] = self.get_father(fa[t], fa)
        return fa[t]

    def killProcess(self, pid, ppid, kill):
        """
        :type pid: List[int]
        :type ppid: List[int]
        :type kill: int
        :rtype: List[int]
        """
        fa = {}
        ans = []
        for i in range(len(pid)):
            fa[pid[i]] = ppid[i]

        fa[kill] = kill

        for i in range(len(pid)):
            par = self.get_father(pid[i], fa)
            if par == kill:
                ans.append(pid[i])
        return ans



