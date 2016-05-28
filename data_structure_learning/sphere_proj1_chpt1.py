from math import pi
class CircleCalculator(object):
    def __init__(self):
        self.radius = float(input('Enter a number for the radius: '))

    def calculate(self):
        diameter = self.radius*2.0
        circumference = diameter*pi
        surface_area = 4*pi*self.radius**2
        volume = 4.0/3*pi*self.radius**3
        print 'The diameter of this circle is %f' % diameter
        print 'The circumference of this circle is %f' % circumference
        print 'The surface area of this circle is %f' % surface_area
        print 'The volume of this circle is %f' % volume

if __name__ == '__main__':
    cc = CircleCalculator()
    cc.calculate()

#DONE
