import math
import cmath
class Quadratic:
    def __init__(self,a,b,c):
        self.a=a
        self.b=b
        self.c=c
    def roots(self):
        discriminant=(self.b**2)-(4*self.a*self.c)
        if discriminant == 0:
            x=-self.b/(2*self.a)
            return [round(x,5)]
        if discriminant > 0:
            x=(-self.b+math.sqrt(self.b**2-4*self.a*self.c))/ (2*self.a)
            x1=(-self.b-math.sqrt(self.b**2-4*self.a*self.c))/ (2*self.a)
            return [round(x,5),round(x1,5)]
        if discriminant < 0:
            value=-discriminant
            x=round(-self.b/(2*self.a),5)+(round((math.sqrt(value))/(2*self.a),5)*cmath.sqrt(-1))
            x1=round(-self.b/(2*self.a),5)-(round((math.sqrt(value))/(2*self.a),5)*cmath.sqrt(-1))
            return [x,x1]
class Cubic:
    def __init__(self,a,b,c,d):
        self.a=a
        self.b=b
        self.c=c
        self.d=d
    def roots(self):
        f=(self.c/self.a)-((self.b*self.b)/(3*self.a*self.a))
        g=(((2*self.b*self.b*self.b)/(self.a*self.a*self.a))-((9*self.b*self.c)/(self.a*self.a))+((27*self.d)/self.a))/27
        h=((g*g)/4)+((f*f*f)/27)
        if f == 0 and g == 0 and h == 0:
            x=(self.d/self.a)**(1/3)*-1
            return [round(x,5)]
        if h <= 0 and f != 0 and g != 0:
            i=math.sqrt((g*g/4)-h)
            j=(i)**(1/3)
            k=math.acos(-g/(2*i))
            L=-j
            M=math.cos(k/3)
            N=math.sqrt(3)*math.sin(k/3)
            P=-(self.b/(3*self.a))
            x=2*j*math.cos(k/3)-(self.b/(3*self.a))
            x1=L*(M+N)+P
            x2=L*(M-N)+P
            if x == x1:
                return [round(x,5),round(x2,5)]
            if x == x2:
                return[round(x,5),round(x1,5)]
            if x1 == x2:
                return[round(x,5),round(x1,5)]
            else:
                return[round(x,5),round(x1,5),round(x2,5)]
        if h > 0:
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
            x=(S+U)-(self.b/(3*self.a))
            x1=round(-((S+U)/2)-(self.b/(3*self.a)),5)+round(((S-U)*(math.sqrt(3)))/2,5)*(cmath.sqrt(-1)) 
            x2=round(-((S+U)/2)-(self.b/(3*self.a)),5)-round(((S-U)*(math.sqrt(3)))/2,5)*(cmath.sqrt(-1)) 
            return[round(x,5),x1,x2]
