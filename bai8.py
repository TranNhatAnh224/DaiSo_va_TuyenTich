from sympy import Symbol
x = Symbol('x')
y = Symbol('y')
bieuthuc = x*x - x*y + y*y
print(bieuthuc)
giatri = bieuthuc.subs({x:3, y:2})
print(giatri)
print(x)
print(y)
giatri = bieuthuc.subs({x:3, y:x})
print(giatri)
giatri = bieuthuc.subs({y:x}).subs({x:3})
print(giatri)
bieuthuc_moi = bieuthuc.subs({x:1-y})
print(bieuthuc_moi)
from sympy import simplify
dongian = simplify(bieuthuc_moi)
print(dongian)
from sympy import sin, cos 
bt = sin(x)*cos(y) + cos(x)*sin(y)
bt_moi = simplify(bt)
print(bt_moi)