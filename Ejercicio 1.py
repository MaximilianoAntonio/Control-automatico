from sympy import symbols, Eq, solve

# Definimos la variable s y los coeficientes A, B, C
s = symbols('s')
A, B, C = symbols('A B C')
    
# Expresion original
lhs = 5*s + 2
    
# Expansion en fracciones parciales
rhs = A*(s+2)**2 + B*(s+1)*(s+2) + C*(s+1)
    
# Expandimos el lado derecho
expanded_rhs = rhs.expand()
    
# Igualamos ambos lados para resolver el sistema de ecuaciones
equations = Eq(lhs, expanded_rhs)
    
# Resolvemos para A, B y C
coefficients = solve(equations, [A, B, C])

# Imprimimos los coeficientes
print(coefficients)
