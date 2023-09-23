import sympy as sp

# Khai báo biến ký hiệu
x, A, B, C = sp.symbols('x A B C')

# Hàm giải phương trình bậc hai
def solve_quadratic(A, B, C):
    equation = A * x**2 + B * x - C
    solutions = sp.solve(equation, x)
    return solutions

# Phương trình 7: Ax^3 - B^3 = 0
A7 = 10
B7 = 11
solutions7 = sp.solve(A7*x**3 - B7**3, x)
print("Solutions for Ax^3 - B^3 = 0:", solutions7)






