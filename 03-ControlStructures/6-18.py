#Let x and y denote the coordinates of a point on the plane.
#Write a program that determines in which quadrant of the coordinate system 
#the point P(x, y) is located or on which axis it is located, or that it is located in 
#the position (0,0) of the coordinate system. 
#Sample result:

#x = 5
#y = 2
#Point P(5,2) is in the first quadrant of the coordinate system

#Niech x i y oznaczają współrzędne punktu na płaszczyźnie.
#Napisz program, który określa, w której ćwiartce układu współrzędnych
#znajduje się punkt P(x, y), na której osi się znajduje, lub że znajduje się on w 
#pozycji (0,0) układu współrzędnych.
#Przykładowy wynik:

#x = 5
#y = 2
#Punkt P(5, 2) znajduje się w pierwszej ćwiartce układu współrzędnych

x = 0
y = 7

if x > 0 and y > 0:
    print(f'Point P({x},{y}) is in the first quadrant of coordinate system')

if x > 0 and y < 0:
    print(f'Point P({x},{y}) is in the fourth quadrant of coordinate system')

if x < 0 and y > 0:
    print(f'Point P({x},{y}) is in the second quadrant of coordinate system')

if x < 0 and y < 0:
    print(f'Point P({x},{y}) is in the third quadrant of coordinate system')

if x == 0 and y > 0 or x == 0 and y < 0:
    print(f'Point P({x},{y}) is located on axis y')

if x > 0 and y == 0 or x < 0 and y == 0:
    print(f'Point P({x},{y}) is located on axis x')

if x ==0 and y ==0:
    print(f'Point P({x},{y}) is located in the position (0,0) of coordinate system')