class Coordinate(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __str__(self):
        return "(" + str(self.x) + ", " + str(self.y) + ")"
    def __cmp__(self, other):
        if other.x == self.x and other.y == self.y:
            return 0
        return -1

class Solution(object):
    def __init__(self):
        pass

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

    def coordinateInList(self, x, y, items):
        for i in items:
            if i.x == x and i.y == y:
                return True
        return False

    def getChildren(self, board, coord, fringe, expanded):
        children = []
        if self.validCoordinate(board, coord.x-1, coord.y) and not self.coordinateInList(coord.x-1, coord.y, expanded):
            children.append(Coordinate(coord.x-1, coord.y))
        if self.validCoordinate(board, coord.x, coord.y-1) and not self.coordinateInList(coord.x, coord.y-1, expanded):
            children.append(Coordinate(coord.x-1, coord.y))
        if self.validCoordinate(board, coord.x+1, coord.y) and not self.coordinateInList(coord.x+1, coord.y, expanded):
            children.append(Coordinate(coord.x+1, coord.y))
        if self.validCoordinate(board, coord.x, coord.y+1) and not self.coordinateInList(coord.x, coord.y+1, expanded):
            children.append(Coordinate(coord.x, coord.y+1))
        return children

    def coordinateListString(self, items):
        items_str = "["
        for i in items:
            items_str += str(i) + ", "
        return items_str[:len(items_str)-2] + "]"

    def countBattleships(self, board):
        battleships = 0
        fringe = [Coordinate(0, 0)]
        expanded = []
        while len(expanded) < (len(board) * len(board[0])):
            visited = fringe.pop(0)
            expanded.append(visited)
            children = self.getChildren(board, visited, fringe, expanded)
            # print("visited:", str(visited))
            # print("expanded:", self.coordinateListString(expanded))
            # print("children:",self.coordinateListString(children))
            # print("fringe:",self.coordinateListString(fringe))
            battleship = False
            if board[visited.x][visited.y] == "X":
                battleship = True
            for c in children:
                if board[c.x][c.y] == "X":
                    battleship = False
                if c not in fringe and c not in expanded:
                    fringe.append(c)
            # print("new_fringe:",self.coordinateListString(fringe))
            if battleship == True:
                battleships += 1
        return battleships

def main():
    test_cases = [["X..X","...X","...X"],
                  ["XXX"],
                  ["X.X"],
                  ["X.X",".X.","X.X"],
                  ["XXX.","...X","...X","....","XXXX"]]

    tester = Solution()

    results = []
    for t in test_cases:
        results.append(tester.countBattleships(t))
    for r in results:
        print(r)

if __name__ == "__main__":
    main()
