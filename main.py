# 1-mashq
def valid_sudoku(board):
    def is_valid_row(row):
        seen = set()
        for num in row:
            if num != ".":
                if num in seen: return False
                seen.add(num)
        return True
    
    for i in range(9):
        if not is_valid_row(board[i]): return False
        if not is_valid_row([board[j][i] for j in range(9)]): return False
    
    for i in range(0,9,3):
        for j in range(0,9,3):
            box = [board[x][y] for x in range(i,i+3) for y in range(j,j+3)]
            if not is_valid_row(box): return False
    return True

board = [
  ["5","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]
print(valid_sudoku(board))
# 2-mashq
def max_profit(prices):
    min_price = float('inf')
    max_profit = 0
    for price in prices:
        min_price = min(min_price, price)
        max_profit = max(max_profit, price - min_price)
    return max_profit

print(max_profit([7,1,5,3,6,4]))
# 3-mashq
def generate_parenthesis(n):
    def backtrack(s, left, right):
        if len(s) == 2 * n:
            result.append(s)
            return
        if left < n:
            backtrack(s + "(", left + 1, right)
        if right < left:
            backtrack(s + ")", left, right + 1)
    
    result = []
    backtrack("", 0, 0)
    return result

print(generate_parenthesis(3))
