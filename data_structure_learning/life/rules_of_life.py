from life import my_neighbors
def item_test(array, row, col):
    count = 0
    neighbors = my_neighbors(row, col)
    for neighbor in neighbors:
        if neighbor:
            count += 1

    if count < 2 or count > 3:
        return False
    elif count == 3:
        return True
