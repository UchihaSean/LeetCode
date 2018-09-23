class Solution(object):
    def exclusiveTime(self, n, logs):
        """
        :type n: int
        :type logs: List[str]
        :rtype: List[int]
        """
        ans = [0 for _ in range(n)]
        stack = []

        for log in logs:
            log_id, state, time = log.split(":")
            log_id, time = int(log_id), int(time)
            if state == 'start':
                stack.append([log_id, 's', time])
            else:
                m_id, m_s, m_t = stack.pop()
                cost = time
                while m_id != log_id or m_s == 'm':
                    cost -= m_t
                    m_id, m_s, m_t = stack.pop()
                ans[log_id] += cost - m_t + 1
                stack.append([log_id, 'm', time - m_t + 1])
        return ans
