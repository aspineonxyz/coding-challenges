class Hourglass:
    def sum_hourglass(y, x):
        hourglass_sum = globals()["matrix"][(y * 6) + x]
        for j in range(y-1,y+2,2):
            for i in range(x-1,x+2):
                hourglass_sum += globals()["matrix"][(j * 6) + i]
        return hourglass_sum

    def max_hourglass(m):
        global matrix
        matrix = m
        for y in range(1,5):
            for x in range(1,5):
                try:
                    max_hourglass = max(max_hourglass, Hourglass.sum_hourglass(y, x))
                except UnboundLocalError:
                    max_hourglass = Hourglass.sum_hourglass(y, x)
        return max_hourglass

class TestHourglass:
    def main():
        matrix = []
        for _ in range(6):
            [matrix.append(int(i)) for i in input().strip().split(' ')]
        print(Hourglass.max_hourglass(matrix))

TestHourglass.main()
