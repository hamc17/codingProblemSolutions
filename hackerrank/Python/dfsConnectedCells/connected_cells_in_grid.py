def maxRegion(grid):
    """Takes in a grid of 1s and 0s and returns the largest connected region size.
    
    Arguments:
        grid {list of lists} -- The grid of 1s and 0s
    
    Returns:
        integer -- The size of the largest connected region.
    """

    return max([regionSize(
        grid, i, j, len(grid), len(grid[0])) for i in xrange(len(grid)) for j in xrange(len(grid[0]))])

def regionSize(grid, i, j, r, c):
    """Finds the region size for cells from [i][j].
    
    Arguments:
        grid {list} -- The grid.
        i {integer} -- The row integer.
        j {integer} -- The column integer.
        r {integer} -- The length of the row.
        c {integer} -- The length of the column.
    
    Returns:
        integer -- The size of the region.
    """

    if i in xrange(r) and j in xrange(c) and grid[i][j] == 1:
        grid[i][j] = 0
        return 1 + sum(regionSize(grid, x, y, r, c) for x in xrange(
            i-1, i+2) for y in xrange(j-1, j+2))
    return 0