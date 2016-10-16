def merge(data_list, l, m, r):
    res = 0

    s1 = data_list[l:m+1]
    s2 = data_list[m+1:r+1]

    i = l
    j = 0
    k = 0

    while j < len(s1) and k < len(s2):
        if s1[j] <= s2[k]:
            data_list[i] = s1[j]
            i += 1
            j += 1
        else:
            data_list[i] = s2[k]
            i += 1
            k += 1
            res = res + len(s1[j:])

    if j < len(s1):
        data_list[i:r+1] = s1[j:]
    else:
        assert (k < len(s2))
        data_list[i:r+1] = s2[k:]

    return res

def merge_new(data_list, l, m, r):
    i = l
    j = m+1
    vec = []
    res = 0
    for k in range(l, r+1):
        if data_list[i] <= data_list[j]:
            vec.append(data_list[i])
            i += 1
        else:
            vec.append(data_list[j])
            j += 1
            res = res + len(data_list[j:r])
    assert len(vec) == r-l+1
    for i in range(len(vec)):
        data_list[l+i] = vec[i]
    return res

class Inversion(object):
    def __init__(self, merge_method=merge):
        self.merge_method = merge_method
        pass
    
    def calculate(self, data_list):
        assert (data_list)
        assert (len(data_list)>0)

        res = self.calculate_rec(data_list, 0, len(data_list)-1)

        return res

    def calculate_rec(self, data_list, l, r):
        assert (data_list)
        assert (l >= 0)
        assert (r < len(data_list))
        assert (l <= r)
        if l == r:
            return 0

        m = (l + r )/2
        assert (m < len(data_list))
        assert (m >= 0) 

        res = 0
        res += self.calculate_rec(data_list, l, m)
        if m+1 < r:
            res += self.calculate_rec(data_list, m+1, r)

        res += self.merge_method(data_list, l, m, r)
        return res
