class Solution(object):
    def validBattleship(self, board, x, y):
        if not board[x][y] == "X":
            return False
        if self.validCoordinate(board, x-1, y) and board[x-1][y] == "X":
            return False
        if self.validCoordinate(board, x, y-1) and board[x][y-1] == "X":
            return False
        return True

    def validCoordinate(self, board, x, y):
        if 0 <= x and x < len(board) and 0 <= y and y < len(board[0]):
            return True
        return False

    def countBattleships(self, board):
        battleships = 0
        for x in range(len(board)):
            for y in range(len(board[0])):
                if self.validBattleship(board, x, y):
                    battleships += 1
        return battleships
