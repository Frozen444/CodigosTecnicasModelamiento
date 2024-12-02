# Importación de librerías necesarias para la creación de la aplicación y los cálculos
import dash
from dash import dcc, html, Input, Output
import numpy as np
from scipy.integrate import odeint
import plotly.graph_objects as go

# Definir el modelo del dengue
def dengue_model(y, t, params):
    # Desempaquetamos las variables del sistema
    S_H, E_H, I_RH, I_DH, R_H, S_V, I_V = y

    # Extraemos los parámetros del diccionario 'params'
    Lambda_H = params['Lambda_H']
    beta_H = params['beta_H']
    mu_H = params['mu_H']
    eta_H = params['eta_H']
    gamma_H1 = params['gamma_H1']
    gamma_H2 = params['gamma_H2']
    theta = params['theta']
    rho = params['rho']
    Lambda_V = params['Lambda_V']
    beta_V = params['beta_V']
    mu_V = params['mu_V']

    # Poblaciones totales humanas y de vectores
    N_H = S_H + E_H + I_RH + I_DH + R_H  # Total de humanos
    N_V = S_V + I_V  # Total de vectores (por ejemplo, mosquitos)

    # Ecuaciones diferenciales para cada grupo de la población
    dS_H_dt = Lambda_H - beta_H * ((S_H * I_V) / N_H) - mu_H * S_H
    dE_H_dt = beta_H * ((S_H * I_V) / N_H) - (eta_H + mu_H) * E_H
    dI_RH_dt = eta_H * E_H - (gamma_H1 + mu_H) * I_RH
    dI_DH_dt = (1 - theta) * gamma_H1 * I_RH - (gamma_H2 + mu_H) * I_DH
    dR_H_dt = theta * gamma_H1 * I_RH + rho * gamma_H2 * I_DH - mu_H * R_H
    dS_V_dt = Lambda_V - beta_V * ((S_V * (I_RH + I_DH)) / N_H) - mu_V * S_V
    dI_V_dt = beta_V * ((S_V * (I_RH + I_DH)) / N_H) - mu_V * I_V

    # Devolvemos la lista de ecuaciones diferenciales
    return [dS_H_dt, dE_H_dt, dI_RH_dt, dI_DH_dt, dR_H_dt, dS_V_dt, dI_V_dt]

# Función para resolver el modelo utilizando scipy's odeint
def solve_dengue_model(params, initial_conditions, t):
    # Resolución del sistema de ecuaciones diferenciales
    return odeint(dengue_model, initial_conditions, t, args=(params,))

# Crear la aplicación Dash
app = dash.Dash(__name__)

# Layout de la aplicación, define cómo se organiza el contenido en la página web
app.layout = html.Div([
    html.Div([
        html.H1("Dinámica del Dengue: Humanos y Mosquitos", style={'text-align': 'center'}),
        html.Div([
            html.Label("Tasa de transmisión humano -> mosquito (β_H):"),
            # Slider para ajustar la tasa de transmisión de humanos a mosquitos
            dcc.Slider(id='beta_H', min=0.1, max=1.0, step=0.1, value=0.5),
        ]),
        html.Div([
            html.Label("Tasa de transmisión mosquito -> humano (β_V):"),
            # Slider para ajustar la tasa de transmisión de mosquitos a humanos
            dcc.Slider(id='beta_V', min=0.1, max=1.0, step=0.1, value=0.3),
        ]),
        html.Div([
            html.Label("Tasa de progresión de expuestos a infecciosos (η_H):"),
            # Slider para ajustar la tasa de progresión de expuestos a infectados en humanos
            dcc.Slider(id='eta_H', min=0.05, max=0.5, step=0.05, value=0.1),
        ]),
    ], style={'width': '25%', 'display': 'inline-block', 'vertical-align': 'top'}),

    html.Div([
        # Gráfico para mostrar la evolución de las poblaciones humanas
        dcc.Graph(id='human-graph', style={'height': '45vh'}),
        # Gráfico para mostrar la evolución de las poblaciones de mosquitos
        dcc.Graph(id='mosquito-graph', style={'height': '45vh'}),
    ], style={'width': '70%', 'display': 'inline-block'}),
])

# Callback que se ejecuta cuando los valores de los sliders cambian
@app.callback(
    [Output('human-graph', 'figure'),
     Output('mosquito-graph', 'figure')],
    [Input('beta_H', 'value'),
     Input('beta_V', 'value'),
     Input('eta_H', 'value')]
)
def update_graph(beta_H, beta_V, eta_H):
    # Definir los parámetros del modelo basados en los valores de los sliders
    params = {
        'Lambda_H': 10, 'beta_H': beta_H, 'mu_H': 0.02, 'eta_H': eta_H,
        'gamma_H1': 0.1, 'gamma_H2': 0.05, 'theta': 0.8, 'rho': 0.6,
        'Lambda_V': 20, 'beta_V': beta_V, 'mu_V': 0.1
    }
    # Condiciones iniciales para las poblaciones
    initial_conditions = [1000, 5, 5, 2, 0, 500, 10]
    # Tiempo de simulación
    t = np.linspace(0, 200, 1000)

    # Resolver el modelo para obtener la evolución de las poblaciones a lo largo del tiempo
    solucion = solve_dengue_model(params, initial_conditions, t)
    S_H, E_H, I_RH, I_DH, R_H, S_V, I_V = solucion.T

    # Crear gráfico para las poblaciones humanas
    human_fig = go.Figure()
    human_fig.add_trace(go.Scatter(x=t, y=S_H, mode='lines', name='S_H'))
    human_fig.add_trace(go.Scatter(x=t, y=E_H, mode='lines', name='E_H'))
    human_fig.add_trace(go.Scatter(x=t, y=I_RH, mode='lines', name='I_RH'))
    human_fig.add_trace(go.Scatter(x=t, y=I_DH, mode='lines', name='I_DH'))
    human_fig.add_trace(go.Scatter(x=t, y=R_H, mode='lines', name='R_H'))
    human_fig.update_layout(title="Poblaciones de Humanos", xaxis_title="Tiempo (días)", yaxis_title="Población")

    # Crear gráfico para las poblaciones de mosquitos
    mosquito_fig = go.Figure()
    mosquito_fig.add_trace(go.Scatter(x=t, y=S_V, mode='lines', name='S_V'))
    mosquito_fig.add_trace(go.Scatter(x=t, y=I_V, mode='lines', name='I_V'))
    mosquito_fig.update_layout(title="Poblaciones de Mosquitos", xaxis_title="Tiempo (días)", yaxis_title="Población")

    # Retornar los gráficos para ser mostrados
    return human_fig, mosquito_fig

# Ejecutar la aplicación web
if __name__ == '__main__':
    app.run_server(debug=True)

