import math

class Shape():
    def __init__(self):
        pass
    def printShapeName(self):
        print('It\'s a Shape')
    def print(self):
        print('It\'s a Shape 0bject')
    def area(self):
        return 0
    def volume(self):
        return 0

class Point(Shape):
    def __init__(self,x , y):
        Shape.__init__(self)
        self.__xPoint = x
        self.__yPoint = y

    def set_y(self,x):
        self.__xPoint = x
    def set_y(self,y):
        self.__yPoint = y 

    def get_x(self):
        return self.__xPoint
    def get_y(self):
        return self.__yPoint

    def printShapeName(self):
        print ('Point: ')
    def print(self):
        print( '(' + format(self.__xPoint, ',.2f') + ',' + format(self.__yPoint, ',.2f') + ')' )

class Circle(Point):
    def __init__(self,x,y,r):
        Point.__init__(self,x,y)
        self.radius = r

    def set_radius(self,r):
        self.radius = r
    def get_radius(self,r):
        return self.radius
        
    def area(self):
        return math.pi*(self.radius*self.radius)

    def printShapeName(self):
        print ('Circle: ')
    def print(self):
       Point.print(self)
       print('Radius: ' , self.radius )

class Cylinder(Circle):
    def __init__(self,x,y,r,h):
        Circle.__init__(self,x,y,r)
        self.height = h

    def set_height(self,h):
        self.height = h
    def get_height(self,h):
        return self.height
        
    def area(self):
        return (2*Circle.area(self) + 2 * math.pi * self.radius *self.height) 
    def volume(self):
        return (Circle.area(self) * self.height)

    def printShapeName(self):
        print ('Cylinder: ')
    def print(self):
       Circle.print(self)
       print('Height: ' , self.height )
        
def main():
    '''xCor = float(input('Enter an X coordinate: '))
    yCor = float(input('Enter a Y coordinate: '))
    rad = float(input('Enter the radius of a Circle: '))
    h = float(input('Enter the height of a Cylinder: '))

    point = Point(xCor,yCor)
    circle = Circle(xCor,yCor, rad)
    cyl = Cylinder(xCor,yCor,rad,h)'''

    point = Point(7,11)
    circle = Circle(3.5,22,8)
    cyl = Cylinder(10,3.3,10,10)

    point.printShapeName()
    point.print()

    circle.printShapeName()
    circle.print()
    print('The area is: ' , format(circle.area(), ',.2f'))

    cyl.printShapeName()
    cyl.print()
    print('The surface area is: ' , format(cyl.area(), ',.2f'))
    print('The volume is: ' , format(cyl.volume(), ',.2f'))

main()

