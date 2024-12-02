import sympy as sp

# Definimos las variables (parámetros y poblaciones)
Lambda_H, Lambda_V, mu_H, mu_V, beta_H, beta_V, eta_H, gamma_H1, gamma_H2, rho, theta, N_H, N_V = sp.symbols(
    'Lambda_H Lambda_V mu_H mu_V beta_H beta_V eta_H gamma_H1 gamma_H2 rho theta N_H N_V')

S_H, E_H, I_RH, I_DH, R_H, S_V, I_V = sp.symbols('S_H E_H I_RH I_DH R_H S_V I_V')

# Definimos las ecuaciones diferenciales del sistema para los puntos críticos
dS_H = Lambda_H - beta_H * (S_H * I_V) / N_H - mu_H * S_H
dE_H = beta_H * (S_H * I_V) / N_H - (mu_H + eta_H) * E_H
dI_RH = eta_H * E_H - (mu_H + gamma_H1) * I_RH
dI_DH = (1 - theta) * gamma_H1 * I_RH - (mu_H + gamma_H2) * I_DH
dR_H = theta * gamma_H1 * I_RH + rho * gamma_H2 * I_DH - mu_H * R_H
dS_V = Lambda_V - mu_V * S_V - beta_V * (S_V * (I_RH + I_DH)) / N_V
dI_V = beta_V * (S_V * (I_RH + I_DH)) / N_V - mu_V * I_V

# Creamos una lista con todas las ecuaciones del sistema
eqs = [dS_H, dE_H, dI_RH, dI_DH, dR_H, dS_V, dI_V]

# Resolvemos el sistema de ecuaciones igualadas a cero para encontrar los puntos críticos
sol = sp.solve(eqs, (S_H, E_H, I_RH, I_DH, R_H, S_V, I_V), dict=True)

# Mostramos las soluciones encontradas
for solution in sol:
    print("Punto crítico encontrado:")
    for var in solution:
        print(f"{var}: {solution[var]}")
    print("\n")

