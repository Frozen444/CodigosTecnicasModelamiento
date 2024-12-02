from sympy import symbols, diff, Matrix

# Definimos las variables del sistema que representan las distintas poblaciones:
# S_H: Susceptibles en humanos, E_H: Expuestos en humanos, I_RH: Infectados recuperados en humanos,
# I_DH: Infectados muertos en humanos, R_H: Recuperados en humanos, S_V: Susceptibles en vectores (por ejemplo, mosquitos),
# I_V: Infectados en vectores.
S_H, E_H, I_RH, I_DH, R_H, S_V, I_V = symbols('S_H E_H I_RH I_DH R_H S_V I_V')

# Definimos los parámetros que modelan las tasas de cambio y las interacciones entre las variables:
# Lambda_H: Tasa de entrada de susceptibles a la población humana,
# beta_H: Tasa de transmisión del virus entre humanos y vectores,
# N_H: Población total de humanos,
# mu_H: Tasa de mortalidad de humanos,
# eta_H: Tasa de exposición a infectados en humanos,
# gamma_H1: Tasa de recuperación de humanos infectados,
# theta: Fracción de humanos recuperados que se trasladan a la categoría de inmunizados,
# gamma_H2: Tasa de mortalidad de humanos infectados,
# rho: Tasa de eliminación de infectados muertos,
# Lambda_V: Tasa de entrada de susceptibles a la población de vectores,
# beta_V: Tasa de transmisión del virus entre vectores y humanos,
# N_V: Población total de vectores,
# mu_V: Tasa de mortalidad de vectores.
Lambda_H, beta_H, N_H, mu_H, eta_H, gamma_H1, theta, gamma_H2, rho = symbols('Lambda_H beta_H N_H mu_H eta_H gamma_H1 theta gamma_H2 rho')
Lambda_V, beta_V, N_V, mu_V = symbols('Lambda_V beta_V N_V mu_V')

# Definimos las ecuaciones diferenciales que modelan las tasas de cambio para cada grupo de población
# Estas ecuaciones representan el modelo dinámico de la propagación de la enfermedad.

# Cambio en la población de susceptibles humanos
dS_H_dt = Lambda_H - beta_H * S_H * I_V / N_H - mu_H * S_H

# Cambio en la población de humanos expuestos
dE_H_dt = beta_H * S_H * I_V / N_H - (mu_H + eta_H) * E_H

# Cambio en la población de humanos infectados que se recuperan
dI_RH_dt = eta_H * E_H - (mu_H + gamma_H1) * I_RH

# Cambio en la población de humanos infectados que mueren
dI_DH_dt = (1 - theta) * gamma_H1 * I_RH - (mu_H + gamma_H2) * I_DH

# Cambio en la población de humanos recuperados
dR_H_dt = theta * gamma_H1 * I_RH + rho * gamma_H2 * I_DH - mu_H * R_H

# Cambio en la población de susceptibles vectores
dS_V_dt = Lambda_V - beta_V * S_V * (I_RH + I_DH) / N_V - mu_V * S_V

# Cambio en la población de vectores infectados
dI_V_dt = beta_V * S_V * (I_RH + I_DH) / N_V - mu_V * I_V

# Creamos una lista que contiene todas las ecuaciones diferenciales
eqs = [dS_H_dt, dE_H_dt, dI_RH_dt, dI_DH_dt, dR_H_dt, dS_V_dt, dI_V_dt]

# Lista con las variables que se están considerando en el modelo
variables = [S_H, E_H, I_RH, I_DH, R_H, S_V, I_V]

# Calculamos la matriz Jacobiana, que contiene las derivadas parciales de las ecuaciones con respecto a las variables
# La matriz Jacobiana ayuda a analizar la estabilidad del sistema dinámico.
jacobiana = Matrix([[diff(eq, var) for var in variables] for eq in eqs])

# Mostramos la matriz Jacobiana calculada
print("Matriz Jacobiana:")
for row in jacobiana:
    print(row)
