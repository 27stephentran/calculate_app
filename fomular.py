import sympy as sp
import logging
logger = logging.Logger("core")

x, a, b, c = sp.symbols('x A B C')


def solve_quadratic(a, b, c):
    equation = a * x**2 + b * x - c
    solutions = sp.solve(equation, x)
    return solutions


#Ax^2 + Bx - C = 0
def solution1(a,b,c):
    solutions1 = solve_quadratic(a, b, c)
    logger.info(f"solution1 {solutions1}")
    return solutions1


#x^2 + 2Ax + A^2 = 0
def solution2(a):
    solutions2 = solve_quadratic(1, 2*a, a**2)
    return solutions2

#x^2 - 2Ax + A^2 = 0
def solution3(a):
    solutions3 = solve_quadratic(1, -2*a, a**2)
    return solutions3

#(Ax + B)^2 * (Ax - B)^2 = 0
def solution4(a, b):
    solutions4 = solve_quadratic(a**2 - b**2, 0, 0)
    return solutions4

# (Ax + B)^3 = 0
def solution5(a,b):
    solutions5 = sp.solve((a*x + b)**3, x)
    return solutions5

# (Ax - B)^3 = 0
def solution6(a,b):
    solutions6 = sp.solve((a*x - b)**3, x)
    return solutions6

# Ax^3 - B^3 = 0
def solution7(a,b):
    solutions7 = sp.solve(a*x**3 - b**3, x)
    return solutions7
