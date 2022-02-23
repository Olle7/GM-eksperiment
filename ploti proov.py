from sympy.plotting import plot
from sympy import symbols
x,a=symbols("x,a")
y=x**2+1+a

y=y.subs(a,10)
print(y)

plot(y, (x, -5, 5))

from sympy.plotting import plot3d
plot3d(x*a, (x, -5, 5), (a, -5, 5))