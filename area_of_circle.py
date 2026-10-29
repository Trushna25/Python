# Area of circle using function under another function

def square(r):
    return r**2

def area_of_circle(r):
    area=3.14 * square(r)
    print(area)

area_of_circle(5)