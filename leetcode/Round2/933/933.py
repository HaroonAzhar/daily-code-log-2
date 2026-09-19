# 933. Number of Recent Calls
class RecentCounter:

    def __init__(self):
        self.q = []

    def ping(self, t: int) -> int:
        while self.q[0] < t - 3000:
            self.q.popleft()
        return len(self.q)