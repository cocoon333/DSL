class TriangleArray():
    def __init__(self, numRows, numCols):
        self.list = []
        sub_list = []
        self.numRows = numRows
        self.numCols = numCols
        for i in xrange(numRows):
            for j in xrange(self.numCols):
                sub_list.append(None)
            self.numCols -= 1
            self.list.append(sub_list)
            sub_list = []
        self.numCols = numCols

    def number_of_rows(self):
        return self.numRows

    def number_of_columns(self):
        return self.numCols

    def clear(self):
        del self.list
        self.__init__(self.numRows, self.numCols)

    def getitem(self, row, column):
        return self.list[row][column]

    def setitem(self, row, column, value):
        self.list[row][column] = value

    def __str__(self):
        return str(self.list)

    def __repr__(self):
        return self.__str__()
