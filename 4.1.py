class Triangle:
    FirstSide = None
    SecondSide = None
    TherdSide = None

    def SetData(self, FirstSide, SecondSide, TherdSide):
        self.FirstSide = FirstSide
        self.SecondSide = SecondSide
        self.TherdSide = TherdSide
    def IsItTriangle(self):
        if self.FirstSide + self.SecondSide > self.TherdSide and self.FirstSide + self.TherdSide > self.SecondSide and self.SecondSide + self.TherdSide > self.FirstSide:
            print("Треугольник с данными сторонами существует", end="\n")
        else:
           print("Такого треугольника не существует", end="\n")
    def FindArea(self):
        s = (self.FirstSide + self.SecondSide + self.TherdSide) / 2
        area = (s * (s - self.FirstSide) * (s - self.SecondSide) * (s - self.TherdSide)) ** 0.5
        print("Площадь данного треугольника: ", area, end="\n")

    def FindPerimeter(self):
        perimeter = self.FirstSide + self.SecondSide + self.TherdSide
        print("Периметр данного треугольника: ", perimeter, end="\n")

print("\n")
Triangle1 = Triangle()
Triangle1.SetData(5, 6,7)
Triangle1.IsItTriangle()
Triangle1.FindArea()
Triangle1.FindPerimeter()
print("\n")

Triangle2 = Triangle()
Triangle2.SetData(1, 8,4)
Triangle2.IsItTriangle()
print("\n")

Triangle3 = Triangle()
Triangle3.SetData(74, 100,84)
Triangle3.IsItTriangle()
Triangle3.FindArea()
Triangle3.FindPerimeter()
print("\n")