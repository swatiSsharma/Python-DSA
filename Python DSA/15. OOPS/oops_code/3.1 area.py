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

    def circle(self, radius) -> str:
        return 'Area of circle: '+ str( 3.14 * (radius ** 2))

    def triangle(self, base, height) -> str:
        return 'Area of triangle: ' + str(0.5 * base * height )

area= Area()
area.rectangle()
print(area.circle(34))
print(area.triangle(67,89))