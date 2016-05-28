def intersect(setA, setB):
    new_set = []
    for element in setA:
        if element in setB:
            new_set.append(element)
    return new_set

def differance(setA, setB):
    new_set = []
    for element in setA:
        if element not in setB:
            new_set.append(element)
    return new_set
