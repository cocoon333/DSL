def unique_item_in_collection(lyst):
    dict = {}
    for element in lyst:
        if element not in dict:
            dict[element] = 1
        else:
            dict[element] += 1
    return len(dict.keys())
