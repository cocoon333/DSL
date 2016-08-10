class inc(object):
    def __init__(self, n):
        n.reverse()
        self.n = n
    def controller(self):
        self.n[0] += 1
        if self.n[0] > 9:
            self.controller_recr(self.n, carry=1)
        self.n.reverse()
        return self.n

    def controller_recr(self, n, carry=0, i=1):
        if carry == 0:
            return True
        else:
            n[0+i] += 1
            n[0+i-1] = 0
            if n[0+i] > 9:
               self.controller_recr(n, carry=1, i=i+1)
            else:
               self.controller_recr(n, i=i+1)
