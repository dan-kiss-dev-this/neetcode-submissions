class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # idea you can check if there is dup in horizontal quick,
        # note the . period is a string
        # are you wanting to use string or int? string due to less converisons
        # if "." ignore

        # note each 3 by 3 box should not have duplicate values also

        #the issue is you are getting the rows, you will also need to check columns
        # this can lead to a lot of for loops wouldn't it help to have a column checker

        # need a way to make the 3 by 3 box and check for dup values, maybe you use a set
        # and see if the set has lower length? issue is the "." values

        #naive start
        # see if row has duplicate values
        # you have to cut the data to pieces and run it

        cols = collections.defaultdict(set)
        rows = collections.defaultdict(set)
        squares = collections.defaultdict(set) # key( row/3, column/3)

        for r in range(9): # 0,1,2,3,4,5,6,7,8
            for c in range(9):
                if board[r][c] == ".":
                    continue
                if(board[r][c] in rows[r] or
                board[r][c] in cols[c] or
                board[r][c] in squares[(r // 3, c // 3)]):
                    return False

                cols[c].add(board[r][c]) # add the value
                # as the value is added here as you go to the next square if a value is already in
                # the set which means we return false
                rows[r].add(board[r][c])
                squares[( r//3, c // 3)].add(board[r][c])
        return True



