
                                                                    #POLYGON AREA CALCULATOR#
                                                                     #PYTHON PROGRAMMING LAB#
                                                                    #DONE BY 20pw01-Abishek.A#
                                                    
class Polygon:
    """A Polygon is a closed figure made up of straight lines
    Represents a polygon.
    Polygon object is initialized with its shape name"""
    
    def __init__(self,shape):
        #Initializes the Polygon object with its shape name
        self.shape = shape

    def define(self):
        #Returns a string stating the shape is a Polygon
        return (self.shape)+" is a closed figure with straight lines"

class Triangle(Polygon):
    """Represents triangle.
    The Triangle object is initialized with its base and height"""

    def __init__(self, base, height, shape):
        #Initializes the Triangle object with its base and height
        self.base = base
        self.height = height
        self.shape = Polygon("Triangle")

    def define(self):
        #A Triangle is a polygon
        return self.shape.define()

    def set_base(self, base):
        #Sets base of the object
        self.base = base

    def set_height(self, height):
        #Sets height of the Triangle object
        self.height = height

    def get_base(self, base):
        #Returns base of the Triangle object
        return self.base

    def get_height(self, height):
        #Returns height of the Triangle object
        return self.height

    def get_area(self):
        #returns area of the Triangle object
        return ((1/2) * self.height * self.base)

    def get_diagonal(self):
        #returns a string saying triangles dont have diagonals
        return "Triangles don't have diagonals."
    def __str__(self):
        #String representation of the Triangle object.
        return "Triangle(base=" + str(self.base) + ", height=" + str(self.height) + ")"

class Rectangle(Polygon):
    """Represents rectangular shapes.
    The Rectangle object is initialized with width and height of the rectangular
    shape. Area, perimeter and diagonal are included."""
    
    def __init__(self, width, height, shape):
        #Initializes the Rectangle object.
        self.width = width
        self.height = height
        self.shape = Polygon("Rectangle")

    def define(self):
        #A rectangle is a polygon
        return self.shape.define()

    def set_width(self, width):
        #Sets width of the Rectangle object.
        self.width = width

    def set_height(self, height):
        #Sets height of the Rectangle object.
        self.height = height

    def get_width(self):
        #Gets width of the Rectangle object.
        return self.width

    def get_height(self):
        #Gets height of the Rectangle object.
        return self.height

    def get_area(self):
        #Gets the area of the Rectangular object.
        return self.width * self.height

    def get_perimeter(self):
        #Gets the perimeter of the Rectangular object.
        return (2 * self.width) + (2 * self.height)

    def get_diagonal(self):
        #Gets the diagonal of the Rectangular object.
        return ((self.width ** 2 + self.height ** 2) ** 0.5)
    
    def __str__(self):
        #String representation of the Rectangle object.
        return "Rectangle(width=" + str(self.width) + ", height=" + str(self.height) + ")"

class Square(Rectangle):
    """Represents square shapes. A square is a rectangle.
    The square object is initialized with a side length."""

    def __init__(self, side, shape):
        #Initializes the Square object.
        Rectangle.__init__(self,side,side,shape)

    def define(self):
        #A Square is a Rectangle so a polygon
        return self.shape.define()

    def set_side(self, side):
        #Sets the sides of the Square object.
        self.width = side
        self.height = side

    def __str__(self):
        #String representation of the Square object.
        return "Square(side=" + str(self.width) + ")" 

n=1
while n!=0:
    print("===============POLYGON AREA CALCULATOR===============")
    print("\nEnter the corresponding number\n")
    print("\t| 1 | To calculate for Triangle")
    print("\t| 2 | To calculate for Rectangle")
    print("\t| 3 | To calculate for Square")
    print("\t| 0 | To calculate for triangle\n")
    n = int(input("Enter your input here: "))

    if (n==1):
        flag = 1
        print("====================TRIANGLE====================")
        height = int(input("Enter height: "))   #Input height
        base = int(input("Enter base: "))       #Input base
        tri = Triangle(base, height, "Triangle")            #creating object for Triangle
        print(tri.define())                     #Triangle is a polygon
        print("Area: ",tri.get_area())          #Displaying necessary details
        print("Length of diagonal: ",tri.get_diagonal())
        print(tri)
        print("\n")

        while flag!=0:
            height = int(input("Enter height to change: "))
            base = int(input("Enter width to change: "))
            tri.set_height(height)
            tri.set_base(base)
            print("Modified area: ",tri.get_area())
            print("Modified length of diagonal: ",tri.get_diagonal())
            print(tri)
            print("\n")
            flag = int(input("ENTER 0 TO EXIT OTHER TO CONTINUE MODIFY THE SHAPE: "))
        flag=1
                       
    elif (n==2):
        print("====================RECTANGLE====================")
        height = int(input("Enter height: "))               #Input height
        width = int(input("Enter width: "))                 #Input width
        rect = Rectangle(width, height, "Rectangle")        #Creating oject for Rectangle
        print(rect.define())                                #Rectangle is a polygon
        print("Area: ",rect.get_area())                     #Displaying necessary details
        print("Perimeter: ",rect.get_perimeter())
        print("Length of diagonal: ",rect.get_diagonal())
        print(rect)
        print("\n")

        while flag!=0:
            height = int(input("Enter height to change: "))
            width = int(input("Enter width to change: "))
            rect.set_height(height)
            rect.set_width(width)
            print("Modified area: ",rect.get_area())
            print("Modified perimeter: ",rect.get_perimeter())
            print("Modified length of diagonal: ",rect.get_diagonal())
            print(rect)
            print("\n")
            flag = int(input("ENTER 0 TO EXIT OTHER TO CONTINUE MODIFY THE SHAPE: "))         
        flag=1

    elif (n==3):
        print("====================SQUARE====================")
        side = int(input("Enter side of square: "))     #Input side
        sq = Square(side,"Square")                      #Creating object for Square
        print(sq.define())                              #Square is a Polygon and a rectangle
        print("Area: ",sq.get_area())                   #Displaying necessary details using inheritance
        print("Perimeter: ",sq.get_perimeter())
        print("Length of diagonal: ",sq.get_diagonal())
        print(sq)
        print("\n")

        while flag!=0:
            side = int(input("Enter side of square to change: "))
            sq.set_side(side)
            print("Modified area: ",sq.get_area())
            print("Modified perimeter: ",sq.get_perimeter())
            print("Modified length of diagonal: ",sq.get_diagonal())
            print(sq)
            print("\n")
            flag = int(input("ENTER 0 TO EXIT OTHER TO CONTINUE MODIFY THE SHAPE: "))
        flag=1

    elif (n==0):
        print("\n\nTHANK YOU FOR USING OUR CALCULATOR\n\n")

    else:
        print("\n\nINVALID INPUT!!\nPlease enter correct input\n\n")
