from sets import Set
def union(setA, setB):
    set1 = Set(setA)
    set2 = Set(setB)
    union_set = set1 | set2
    return union_set

def interset(setA, setB):
    set1 = Set(setA)
    set2 = Set(setB)
    intersection_set = set1 & set2
    return intersection_set

def difference(setA, setB):
    set1 = Set(setA)
    set2 = Set(setB)
    difference_set = setA - setB
    return difference_set

def isSubsetOf(setA, setB):
    set1 = Set(setA)
    set2 = Set(setB)
    subset_or_not = set1.issubset(set2)
    return subset_or_not
