from triangle import Triangle

a = None
b = None
c = None

try:
    a = int(input('Enter side a: '))
    b = int(input('Enter side b: '))
    c = int(input('Enter side c: '))
except ValueError as e:
    print(e, '\r: Wrong values. Try again.')

triangle = Triangle()
print(f'Triangle\'s area: {triangle.area(a, b, c)}')