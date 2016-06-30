from list_implementation import List
def item_test(array, row, col):
    count = 0
    neighbors = my_neighbors(array, row, col)
    for neighbor in neighbors:
        if array[neighbor[0]][neighbor[1]] == 1:
            count += 1
    if count < 2 or count > 3:
        return 0
    elif count == 3:
        return 2
    return 1

def my_neighbors(array, row, col):
    neighbors = List()
    border_type = is_border(array, row, col)
    corner_type = is_corner(array, row, col)
    if corner_type:
        if corner_type == 1:
            neighbors.append([row, col+1])
            neighbors.append([row+1, col+1])
            neighbors.append([row+1, col])
        elif corner_type == 2:
            neighbors.append([row-1, col])
            neighbors.append([row-1, col+1])
            neighbors.append([row, col+1])

        elif corner_type == 3:
            neighbors.append([row, col-1])
            neighbors.append([row-1, col-1])
            neighbors.append([row-1, col])

        elif corner_type == 4:
            neighbors.append([row, col-1])
            neighbors.append([row+1, col-1])
            neighbors.append([row+1, col])

    elif border_type:
        if border_type == 1:
            neighbors.append([row-1, col])
            neighbors.append([row-1, col-1])
            neighbors.append([row, col-1])
            neighbors.append([row+1, col-1])
            neighbors.append([row+1, col])

        elif border_type == 2:
            neighbors.append([row, col+1])
            neighbors.append([row-1, col+1])
            neighbors.append([row-1, col])
            neighbors.append([row-1, col-1])
            neighbors.append([row, col-1])

        elif border_type == 3:
            neighbors.append([row+1, col])
            neighbors.append([row+1, col+1])
            neighbors.append([row, col+1])
            neighbors.append([row-1, col+1])
            neighbors.append([row-1, col])

        elif border_type == 4:
            neighbors.append([row, col-1]) 
            neighbors.append([row+1, col-1])
            neighbors.append([row+1, col])
            neighbors.append([row+1, col+1])
            neighbors.append([row, col+1])

    else:
        #not corner or border
        for i in range(row-1, row+2):
            for j in range(col-1, col+2):
                if i == row and j == col:
                    # do nothing for itself
                    pass
                else:
                    neighbors.append([i, j])
    return neighbors

def is_corner(array, row, col):
    if row == 0 and col == 0:
        return 1
    elif row == len(array)-1 and col == 0:
        return 2
    elif row == len(array)-1 and col == len(array[0])-1:
        return 3
    elif row == 0 and col == len(array[0])-1:
        return 4
    return False

def is_border(array, row, col):
    if col == len(array[0])-1:
        return 1
    elif row == len(array)-1:
        return 2
    elif col == 0:
        return 3
    elif row == 0:
        return 4
    return False
