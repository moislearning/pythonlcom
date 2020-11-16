class Point:
    def __init__(self,
                 x=0, y=0):
        """ Create a new point at x, y """
        self.x = x
        self.y = y

    def __str__(self):
        return "Point(%s,%s)" % (self.x, self.y)

    def distance(p, q):
        dx = q.x - p.x
        dy = q.y - p.y
        dsquared = dx * dx + dy * dy
        result = dsquared ** 0.5
        return result

    def reflect_t(self):
        self.y = -self.y
        pr = Point(self.x, self.y)
        return pr

    def slope(p, q):
        if p.y - q.y and p.x - q.x != 0:
            m = (p.y - q.y) / (p.x - q.x)
            return m
        else:
            return print("Slope is 0 or indefinite")

    def intercept(p, q):
        if (p.x - q.x) != 0:
            b = (p.x * q.y - q.x * p.y) / (p.x - q.x)
            return b
        else:
            return print("No interception with y-axis")

    def equation(p, q):
        b = Point.intercept(p, q)
        m = Point.slope(p, q)
        return print("Equation: f(x) = {} * X + {}".format(b, m))


p1 = Point(1, 2)
p2 = Point(2, 3)
p3 = Point(3, 4)
p4 = Point(4, 5)

print(Point.distance(p1, p2))

print(Point.reflect_t(p1))

print(Point.slope(p1, p2))

print(Point.intercept(p1, p2))

Point.equation(p1, p2)