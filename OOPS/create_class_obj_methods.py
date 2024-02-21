class CircleCalculations:
    pie=3.14
    def __init__(self,radius):
        self.radius = radius
    def calc_area(self):
        area=CircleCalculations.pie*self.radius**2
        print(f"Area of circle is {area}")
    def calc_circumference(self):
        circumference=2*CircleCalculations.pie*self.radius
        print(f"Circumference is  {circumference}")

cc=CircleCalculations(7)
cc.calc_area()
cc.calc_circumference()