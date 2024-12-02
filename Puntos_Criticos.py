# Importamos la librería SymPy para trabajar con álgebra simbólica y ecuaciones diferenciales
import sympy as sp

# Definimos las variables simbólicas para los parámetros del modelo y las poblaciones involucradas
Lambda_H, Lambda_V, mu_H, mu_V, beta_H, beta_V, eta_H, gamma_H1, gamma_H2, rho, theta, N_H, N_V = sp.symbols(
    'Lambda_H Lambda_V mu_H mu_V beta_H beta_V eta_H gamma_H1 gamma_H2 rho theta N_H N_V')

# Definimos las variables simbólicas para las poblaciones humanas y de mosquitos
S_H, E_H, I_RH, I_DH, R_H, S_V, I_V = sp.symbols('S_H E_H I_RH I_DH R_H S_V I_V')

# Definimos las ecuaciones diferenciales del modelo, las cuales describen la evolución de las poblaciones
# para los puntos críticos (cuando las derivadas son iguales a cero)

# Cambio en la población susceptible de humanos (S_H)
dS_H = Lambda_H - beta_H * (S_H * I_V) / N_H - mu_H * S_H

# Cambio en la población de humanos expuestos (E_H)
dE_H = beta_H * (S_H * I_V) / N_H - (mu_H + eta_H) * E_H

# Cambio en la población de humanos infectados (I_RH)
dI_RH = eta_H * E_H - (mu_H + gamma_H1) * I_RH

# Cambio en la población de humanos infectados con dengue grave (I_DH)
dI_DH = (1 - theta) * gamma_H1 * I_RH - (mu_H + gamma_H2) * I_DH

# Cambio en la población de humanos recuperados (R_H)
dR_H = theta * gamma_H1 * I_RH + rho * gamma_H2 * I_DH - mu_H * R_H

# Cambio en la población susceptible de mosquitos (S_V)
dS_V = Lambda_V - mu_V * S_V - beta_V * (S_V * (I_RH + I_DH)) / N_V

# Cambio en la población de mosquitos infectados (I_V)
dI_V = beta_V * (S_V * (I_RH + I_DH)) / N_V - mu_V * I_V

# Creamos una lista con todas las ecuaciones del sistema
eqs = [dS_H, dE_H, dI_RH, dI_DH, dR_H, dS_V, dI_V]

# Usamos la función 'solve' de SymPy para resolver el sistema de ecuaciones igualadas a cero,
# lo cual nos dará los puntos críticos (es decir, los valores de las poblaciones en equilibrio).
sol = sp.solve(eqs, (S_H, E_H, I_RH, I_DH, R_H, S_V, I_V), dict=True)

# Mostramos las soluciones encontradas para los puntos críticos
for solution in sol:
    print("Punto crítico encontrado:")  # Imprimimos la cabecera indicando que es un punto crítico
    # Iteramos sobre las variables y mostramos sus valores en cada punto crítico encontrado
    for var in solution:
        print(f"{var}: {solution[var]}")  # Mostramos el valor de cada variable en el punto crítico
    print("\n")  # Salto de línea entre diferentes puntos críticos

