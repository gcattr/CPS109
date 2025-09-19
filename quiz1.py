# jason kwan cps109_lab1.py
import math


# question 1
print("temperature test")
# temperature
def Kelvin(Celsius):
    return Celsius + 273.15

def Fahrenheit(Celsius):
    return (Celsius * 9/5) + 32

CelsiusInput = float(input("enter temperature in celsius: "))
print(f"{CelsiusInput}°C is {Kelvin(CelsiusInput)}K")
print(f"{CelsiusInput}°C is {Fahrenheit(CelsiusInput)}°F")


# question 2
print("---------------------- \nquadratic formula test ")
# quadratic formula
def Quadratic(A, B, C):
    Discriminant = (B**2) - (4*A*C)
    if Discriminant < 0:
        return "no real roots"
    elif Discriminant == 0:
        Root = -B / (2*A)
        return f"root: {Root}"
    else:
        Root1 = (-B + Discriminant**0.5) / (2*A)
        Root2 = (-B - Discriminant**0.5) / (2*A)
        return f"roots: {Root1} and {Root2}"

A = float(input("enter a: "))
B = float(input("enter b: "))
C = float(input("enter c: "))
print(Quadratic(A, B, C))
    

#question 3
print("---------------------- \nlegal triangle test")
# legal triangle
def IsALegalTriangle(A, B, C):
    return (A + B > C) and (A + C > B) and (B + C > A)

A = float(input("enter side a: "))
B = float(input("enter side b: "))
C = float(input("enter side c: "))

print(f"is a legal triangle: {IsALegalTriangle(A, B, C)}")


# question 4
print("---------------------- \npentagon area test")
# pentagon area finder
def PentagonArea(l):
    return (1/4) * math.sqrt(5 * (5 + 2 * math.sqrt(5))) * l**2

Length = float(input("enter side length of a pentagon: "))
print(f"the area of the pentagon: {PentagonArea(Length)}")


# question 5
print("---------------------- \ngolden ratio and fibbonacci test")
# nth fib number of golden ratio

GR = (1+ math.sqrt(5)) / 2

def Fibonacci(N):
    return int(round(((2+GR)/5) * (GR**N) + ((3-GR)/5) * (GR**(-N))))

N = int(input("enter the nth fibbonacci number you want:"))
print(f"the {N}th fibbonacci number is: {Fibonacci(N)}")
