''' Triangle class module '''
class Triangle:
    ''' Triangle utilities '''
    def __init__(self) -> None:
        ''' Initializer left empty on purpose. Use class methods instead. '''
        pass

    def side_getter(self, side:str) -> float:
        ''' Returns a side with a symbolic representation '''
        return int(input(f'Enter side {side}: '))

    def area(self, a_side:int, b_side:int, c_side:int) -> float:
        ''' Calculate area of a triangle by Heron's method '''
        calc_s = (a_side + b_side + c_side) / 2 # Semiperimeter
        return (calc_s * (calc_s - a_side) * (calc_s - b_side) * (calc_s - c_side))**(1/2)

if __name__ == '__main__':
    triangle = Triangle()
    triangle_area = triangle.area(
        triangle.side_getter("a"), triangle.side_getter("b"), triangle.side_getter("c"))

    print(f'Triangle area: {triangle_area}')
