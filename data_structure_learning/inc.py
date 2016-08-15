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

class incrementer(object):
    def __init__(self):
        pass

    def vec_to_int(self, v):
        n = 0
        v.reverse()
        for i in xrange(len(v)):
            n = n + v[i] * 10**i
        return n

    def to_vec(self, n):
        '''n: an integer
           return a list, each element is one digit of n
           for example, n = 109, return [1, 0, 9]
        '''
        assert (n >= 0)
        v = []
        while n > 0:
            d = n % 10
            v.insert(0, d)
            n = n / 10
        if not v:
            assert (n == 0)
            v = [0]
        return v

    def inc(self, n, base_of_number=10):
        '''n: an integer
           return n + 1
        '''
        v = self.to_vec(n)
        (v[-1], carry) = self.add(v[-1], 1, base_of_number)
        for i in range(len(v)-2, -1, -1):
            if carry == 0:
                break
            (v[i], carry) = self.add(v[i], carry, base_of_number)
        if carry == 1:
            v.insert(0, 1)
        return self.vec_to_int(v)

    def add(self, augend, addend, base_of_number):
        '''
           return (sum, carry)
        '''
        assert (augend < base_of_number)
        assert (augend >= 0)
        assert (addend < base_of_number)
        assert (addend >= 0)
        s = augend + addend
        carry = s / base_of_number
        s = s % base_of_number
        return (s, carry)
