from math import exp,pow,log,sin
def f(x:int):
    return exp(-x)-sin(x)
def is_replacable(p,q):
    return f(p)*f(q)>0

tol=1e-5

def bisection(a,b):
    k=0
    x=f(a)*f(b)
    if x>0:
        print('choose different a,b')
        return None
    elif x==0:
        if f(a)==0:
            return a
        else: return b
    else:
        while abs(a-b)>tol:
            x=(a+b)/2
            if is_replacable(a,x):a=x
            else: b=x
            k+=1

        return k

def falsi(a,b):
    x=f(a)*f(b)
    k=0
    if x>0:
        print('choose different a,b')
        return None
    elif x==0:
        if f(a)==0:
            return a
        else: return b
    else:
        x=(a*f(b)-b*f(a))/(f(b)-f(a))
        while abs(f(x))>tol:

            if is_replacable(a,x):a=x
            else: b=x
            x=(a*f(b)-b*f(a))/(f(b)-f(a))
            k+=1
        return k

def fixed(a):
    x=f(a)
    if x==0:
        if f(a)==0:
            return a
    else:
        while abs(a-x)>tol:
            a=x
            x=f(x)

        return x

print(bisection(3,4)-falsi(3,4))
