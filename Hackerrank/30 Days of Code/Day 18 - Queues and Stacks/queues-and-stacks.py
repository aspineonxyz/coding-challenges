class Solution:
    def __init__(self):
        self.s = []
        self.q = []
    def pushCharacter(self, ch):
        self.s.append(ch)
    def enqueueCharacter(self, ch):
        self.q.insert(0, ch)
    def popCharacter(self):
        return self.s.pop(len(self.s)-1)
    def dequeueCharacter(self):
        return self.q.pop(len(self.q)-1)
