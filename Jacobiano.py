from sympy import symbols, diff, Matrix

# Definimos las variables
S_H, E_H, I_RH, I_DH, R_H, S_V, I_V = symbols('S_H E_H I_RH I_DH R_H S_V I_V')
# Definimos los parámetros
Lambda_H, beta_H, N_H, mu_H, eta_H, gamma_H1, theta, gamma_H2, rho = symbols('Lambda_H beta_H N_H mu_H eta_H gamma_H1 theta gamma_H2 rho')
Lambda_V, beta_V, N_V, mu_V = symbols('Lambda_V beta_V N_V mu_V')

# Definimos las ecuaciones del sistema
dS_H_dt = Lambda_H - beta_H * S_H * I_V / N_H - mu_H * S_H
dE_H_dt = beta_H * S_H * I_V / N_H - (mu_H + eta_H) * E_H
dI_RH_dt = eta_H * E_H - (mu_H + gamma_H1) * I_RH
dI_DH_dt = (1 - theta) * gamma_H1 * I_RH - (mu_H + gamma_H2) * I_DH
dR_H_dt = theta * gamma_H1 * I_RH + rho * gamma_H2 * I_DH - mu_H * R_H
dS_V_dt = Lambda_V - beta_V * S_V * (I_RH + I_DH) / N_V - mu_V * S_V
dI_V_dt = beta_V * S_V * (I_RH + I_DH) / N_V - mu_V * I_V

# Creamos una lista con todas las ecuaciones
eqs = [dS_H_dt, dE_H_dt, dI_RH_dt, dI_DH_dt, dR_H_dt, dS_V_dt, dI_V_dt]
variables = [S_H, E_H, I_RH, I_DH, R_H, S_V, I_V]

# Calculamos la matriz Jacobiana
jacobiana = Matrix([[diff(eq, var) for var in variables] for eq in eqs])

# Mostramos la matriz Jacobiana
print("Matriz Jacobiana:")
for row in jacobiana:
    print(row)
