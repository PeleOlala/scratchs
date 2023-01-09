def check_rows(grid, i, j):
    cond = [n + 1 for n in range(9)]
    lin1 = [grid[i][k] for k in range(9)]
    lin2 = [grid[k][j] for k in range(9)]
    lin3 = [grid[k + (i // 3) * 3][m + (j // 3) * 3] for k in range(3) for m in range(3)]
    candidat = []
    for r in cond:
        if r not in lin1 and r not in lin2 and r not in lin3:
            candidat.append(r)
    return (len(candidat) == 1, candidat[0])


def naked_single_rec(prev, grid):
    control = True
    if not prev:
        return (False, None)
    for l in grid:
        control = control and 0 not in l
    if control:
        return (True, grid)
    else:
        for i in range(9):
            for j in range(9):
                if grid[i][j] == 0:
                    rescheck = check_rows(grid, i, j)
                    if rescheck[0]:
                        grid[i][j] = rescheck[1]
                        return naked_single_rec(True, grid)
        return (False, None)


def naked_single(grid):
    return naked_single_rec(True, grid)

print(naked_single([[4, 0, 3, 0, 9, 6, 0, 1, 0], 
                    [0, 0, 2, 8, 0, 1, 0, 0, 3], 
                    [0, 1, 0, 0, 0, 0, 0, 0, 7], 
                    [0, 4, 0, 7, 0, 0, 0, 2, 6], 
                    [5, 0, 7, 0, 1, 0, 4, 0, 9], 
                    [1, 2, 0, 0, 0, 3, 0, 8, 0], 
                    [2, 0, 0, 0, 0, 0, 0, 7, 0], 
                    [7, 0, 0, 2, 0, 9, 8, 0, 0], 
                    [0, 6, 0, 1, 5, 0, 3, 0, 2]]))
print(naked_single([[0, 0, 6, 0, 4, 0, 1, 0, 0], 
                    [0, 5, 0, 0, 9, 0, 0, 6, 0], 
                    [8, 0, 0, 0, 0, 0, 0, 0, 5], 
                    [0, 0, 0, 3, 0, 4, 0, 0, 0], 
                    [3, 1, 0, 0, 0, 0, 0, 4, 8], 
                    [0, 0, 0, 8, 0, 7, 0, 0, 0], 
                    [6, 0, 0, 0, 0, 0, 0, 0, 9], 
                    [0, 2, 0, 0, 3, 0, 0, 5, 0], 
                    [0, 0, 1, 0, 5, 0, 7, 0, 0]]))
