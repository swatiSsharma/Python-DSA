'''
Make a class named area

There are no attributes related to area

But it should have 4 methods
- rectangle: l, b -> input
- square: s -> input
- circle: r -> parameter
- triangle: b, h -> parameter
'''

class Area:

    def rectangle(self) -> None:
        length = int(input("Enter the length: "))
        breadth = int(input("Enter the breadth: "))
        print('Area of rectangle',length * breadth)

    def square(self) -> None:
        side = int(input("Enter the side of square: "))
        print('Area of square',side ** 2)

    def circle(self, radius) -> None:
        print('Area of circle: ', 3.14 * (radius ** 2))

    def triangle(self, base, height) -> None:
        print('Area of triangle: ',0.5 * base * height )

area= Area()
area.rectangle()
area.circle(34)