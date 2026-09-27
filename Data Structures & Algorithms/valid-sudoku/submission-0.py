class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        dicR=collections.defaultdict(set)
        dicC=collections.defaultdict(set)
        dicS=collections.defaultdict(set)
        for r in range(9):
            for c in range(9):
                if board[r][c]=='.':
                    continue
                if board[r][c] in dicR[r]:
                    return False
                if board[r][c] in dicC[c]:
                    return False
                if board[r][c] in dicS[r//3, c//3]:
                    return False             

                dicR[r].add(board[r][c])
                dicC[c].add(board[r][c])
                dicS[r//3,c//3].add(board[r][c])

        return True        