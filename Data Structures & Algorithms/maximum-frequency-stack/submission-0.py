class FreqStack:

    def __init__(self):
        self.cnt = {}
        self.mxcnt = 0
        self.stack = {}
    def push(self, val: int) -> None:
        valCnt = 1 + self.cnt.get(val, 0)
        self.cnt[val] = valCnt
        if valCnt > self.mxcnt:
            self.mxcnt = valCnt
            self.stack[valCnt] = []
        self.stack[valCnt].append(val)

    def pop(self) -> int:
        res = self.stack[self.mxcnt].pop()
        self.cnt[res] -= 1
        if not self.stack[self.mxcnt]:
            self.mxcnt -= 1
        return res


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()