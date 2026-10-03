class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        if target == "0000":
            return 0

        if "0000" in deadends:
            return -1

        visit = set(deadends)
        q = deque()
        q.append(("0000", 0))

        def turnlock(lock):
            res = []
            for i in range(4):
                digit = str((int(lock[i])+1)%10)
                res.append(lock[:i]+digit+lock[i+1:])
                digit = str((int(lock[i])-1)%10) 
                res.append(lock[:i]+digit+lock[i+1:])
            return res

        while q:
            lock, turn = q.popleft()
            if lock == target:
                return turn

            for lock in turnlock(lock):
                if lock not in visit:
                    q.append((lock, turn+1))
                    visit.add(lock)

        return -1

        