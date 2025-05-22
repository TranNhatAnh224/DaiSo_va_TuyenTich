from sympy import Symbol # Giả sử đã import
x = Symbol('x')
y = Symbol('y')
s = x*y + y*x
print(s)
p = x*(x + 2*x)
print(p)
p = (x+2)*(y+3) + (x+2)*(x-3)
print(p)
p = x*(-x + 2*x - x)
print(p)
p = (x+2)*(y+3)
print(p.expand())
from sympy import expand
bieuthuc = (x - y)*(x**2 + x*y + y**2)
print(expand(bieuthuc))
from sympy import expand
bieuthuc = (x - y)*(x**2 + x*y + y**2)
print(expand(bieuthuc))
