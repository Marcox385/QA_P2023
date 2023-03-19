''' Main test module for triangle class '''
from triangle import Triangle

A = None
B = None
C = None

try:
    A = int(input('Enter side a: '))
    B = int(input('Enter side b: '))
    C = int(input('Enter side c: '))
except ValueError as e:
    print(e, '\r: Wrong values. Try again.')

triangle = Triangle()
print(f'Triangle\'s area: {triangle.area(A, B, C)}')
