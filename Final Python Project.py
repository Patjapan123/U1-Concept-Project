import math
import cmath
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
    discriminant=(b**2)-(4*a*c)
    if discriminant == 0:
        print("There is one real root")
        x=-b/(2*a)
        print("The value of x is",round(x,5))
    if discriminant > 0:
        print("There are two real roots")
        x=(-b+math.sqrt(b**2-4*a*c))/ 2*a
        x1=(-b-math.sqrt(b**2-4*a*c))/ 2*a
        print("The value of x are", round(x,5),"and",round(x1,5))
    if discriminant < 0:
        value=-discriminant
        print("There are two complex roots")
        x=round(-b/(2*a),5)+(round((math.sqrt(value))/(2*a),5)*cmath.sqrt(-1))
        x1=round(-b/(2*a),5)-(round((math.sqrt(value))/(2*a),5)*cmath.sqrt(-1))
        print("The value of x are",x,"and",x1)
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
    f=(c/a)-((b*b)/(3*a*a))
    g=(((2*b*b*b)/(a*a*a))-((9*b*c)/(a*a))+((27*d)/a))/27
    h=((g*g)/4)+((f*f*f)/27)
    if f == 0 and g == 0 and h == 0:
        print("There is one real root and they are all equal")
        x=(d/a)**(1/3)*-1
        print("The value of x is",round(x,5))
    if h <= 0 and f != 0 and g != 0:
        print("All three roots are real")
        i=math.sqrt((g*g/4)-h)
        j=(i)**(1/3)
        k=math.acos(-g/(2*i))
        L=-j
        M=math.cos(k/3)
        N=math.sqrt(3)*math.sin(k/3)
        P=-(b/(3*a))
        x=2*j*math.cos(k/3)-(b/(3*a))
        x1=L*(M+N)+P
        x2=L*(M-N)+P
        if x == x1:
            print("Two of the roots are the same which is",round(x,5))
            print("The values of x are",round(x,5),"and",round(x2,5))
        if x == x2:
            print("Two of the roots are the same which is",round(x,5))
            print("The values of x are",round(x,5),"and",round(x1,5))
        if x1 == x2:
            print("Two of the roots are the same which is",round(x1,5))
            print("The values of x are",round(x,5),"and",round(x1,5))
        else:
            print("The values of x are",round(x,5),",",round(x1,5),"and",round(x2,5))
    if h > 0:
        print("Only 1 real root and two complex roots")
        R=-(g/2)+math.sqrt(h)
        if R < 0:
            S=-(abs(R))**(1/3)
        if R > 0:
            S=(R)**(1/3)
        T=-(g/2)-math.sqrt(h)
        if T < 0:
            U=-(abs(T))**(1/3)
        if T > 0:
            U=(T)**(1/3)
        x=(S+U)-(b/(3*a))
        x1=round(-((S+U)/2)-(b/(3*a)),5)+round(((S-U)*(math.sqrt(3)))/2,5)*(cmath.sqrt(-1)) 
        x2=round(-((S+U)/2)-(b/(3*a)),5)-round(((S-U)*(math.sqrt(3)))/2,5)*(cmath.sqrt(-1)) 
        print("The value of x are",round(x,5),",",x1,"and",x2)