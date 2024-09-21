from sympy import Matrix, eye, symbols, simplify
import pprint

# Definir las matrices y la variable s
s = symbols('s')
A = Matrix([[0, 1, 0], [0, 0, 1], [-2, -4, -6]])
B = Matrix([[0, 0], [0, 1], [1, 0]])
C = Matrix([[1, 0, 0], [0, 1, 0]])
D = Matrix([[0, 0], [0, 0]])
I = eye(3)  # Matriz identidad de 3x3

# Calcular (sI - A) y su inversa
sI_A_inv = (s * I - A).inv()

print('(sI - A)^(-1) =', sI_A_inv)

# Calcular la función de transferencia G(s) = C(sI - A)^(-1)B + D
G_s = simplify(C * sI_A_inv * B + D)

print('C(sI - A)^(-1)B + D =', G_s)