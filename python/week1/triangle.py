import math

def area(base, height):
  return base * height / 2

def perimeter(side1, side2, side3):
  return side1 + side2 + side3

def semiperimeter(side1, side2, side3):
  return perimeter(side1, side2, side3) / 2

def area_hero(side1, side2, side3):
  ''' (number, number, number) -> float

  return the area of a triangle with sides of length
  side1, side2, side3

  >>> area_hero(3, 4, 5)
  6.0
  >>> area_hero(10.5, 6, 9.3)
  27.73168584850189
  '''

  semi = semiperimeter(side1, side2, side3)
  area = math.sqrt(semi * (semi - side1) * (semi - side2) * (semi - side3))
  return area
