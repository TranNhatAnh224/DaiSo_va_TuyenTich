from sympy import Symbol, solve
x = Symbol('x') # Đã định nghĩa
ptb2 = x**2 + 9*x +8
pt1 = solve(ptb2, dict = True)
print(pt1)
ptb2 = x**2 + 1*x + 10
nghiemx = solve(ptb2, dict = True)
print(nghiemx)
a = Symbol('a')
b = Symbol('b')
c = Symbol('c')
ptb2 = a*x*x + b*x + c
nghiem = solve(ptb2, x, dict=True)
print(nghiem)