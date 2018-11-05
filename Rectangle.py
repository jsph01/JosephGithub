class rectangle:
    def __init__(self, l, w):
        self.length = l
        self.width = w

    def area(self):
        return self.length * self.width

class square(rectangle):
    def perimeter(self):
        return 2*(self.width+self.width)


def main():
    sq = square(5,5)
    print("Area =",sq.area())
    print("Perimeter =", sq.perimeter())

main()