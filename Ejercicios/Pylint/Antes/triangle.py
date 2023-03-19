class Triangle:
    ''' Triangle utilities '''
    def __init__(self) -> None:
        pass

    def side_getter(self, side:str) -> float:
        ''' Returns a side with a symbolic representation '''
        return int(input(f'Enter side {side}: '))

    def area(self, a:int, b:int, c:int) -> float:
        ''' Calculate area of a triangle by Heron's method '''
        p = (a + b + c) / 2 # Semiperimeter
        return (p * (p - a) * (p - b) * (p - c))**(1/2)

if __name__ == '__main__':
    triangle = Triangle()

    print(f'Triangle area: {triangle.area(triangle.side_getter("a"), triangle.side_getter("b"), triangle.side_getter("c"))}')