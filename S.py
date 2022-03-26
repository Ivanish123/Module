import math

def rectangle(lengt, width):
    return(lengt * width)

def triangle(a ,b, c):
    p = (a + b + c )/ 2
    return (p*(p-a)*(p-b)*(p-c))**0.5

def circle(r):
    return (3.14*r**2)
