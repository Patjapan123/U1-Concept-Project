from roots import Quadratic
from roots import Cubic

print("This is a cubic and quadratic calculator")
print("Is this function Quadratic or Cubic?")
function=input()
if function == "Quadratic":
    print("ax^2+bx+c")
    print("Input the value of each variable")
    print("Input a")
    a=int(input())
    print("Input b")
    b=int(input())
    print("Input c")
    c=int(input())
    func = Quadratic(a,b,c)
    discriminant=(b**2)-(4*a*c)
    if discriminant == 0:
        print("There is one real root")
        for i in func.roots():
            print("root:",i)
    if discriminant > 0:
        print("There are two real roots")
        for i in func.roots():
            print("root:",i)
    if discriminant < 0:
        value=-discriminant
        print("There are two complex roots")
        for i in func.roots():
            print("root:",i)
if function == "Cubic":
    print("ax^3+bx^2+cx+d")
    print("Input the value of each variable")
    print("Input a")
    a=int(input())
    print("Input b")
    b=int(input())
    print("Input c")
    c=int(input())
    print("Input d")
    d=int(input())
    func1 = Cubic(a,b,c,d)
    f=(c/a)-((b*b)/(3*a*a))
    g=(((2*b*b*b)/(a*a*a))-((9*b*c)/(a*a))+((27*d)/a))/27
    h=((g*g)/4)+((f*f*f)/27)
    if f == 0 and g == 0 and h == 0:
        print("There is one real root and they are all equal")
        for i in func1.roots():
            print("root:",i)
    if h <= 0 and f != 0 and g != 0:
        print("All three roots are real")
        for i in func1.roots():
            print("root:",i)
    if h > 0:
        print("Only 1 real root and two complex roots")
        for i in func1.roots():
            print("root:",i)