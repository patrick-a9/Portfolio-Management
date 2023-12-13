import sqlite3
import pandas as pd
import requests
from bs4 import BeautifulSoup
from scipy.optimize import minimize
import numpy as np
import warnings


warnings.filterwarnings('ignore')

# Conecta con la base de datos SQLite
conn = sqlite3.connect('api.sqlite')
cursor = conn.cursor()

# Supongamos que tienes una tabla llamada 'tus_datos' y la columna de tickers se llama 'Ticker'
tabla = 'Tickers'
columna_ticker = 'tickers'
columna_id = 'id'

# Obtén los registros desde la base de datos
query = f"SELECT {columna_ticker}, {columna_id} FROM {tabla}"
df = pd.read_sql_query(query, conn)

# Convierte los valores separados por comas en listas
df[columna_ticker] = df[columna_ticker].str.split(',')

# Cierra la conexión con la base de datos
conn.close()

# Diccionario para almacenar los resultados
resultados_por_id = {}
covarianza_por_id = {}
estadisticas_por_id = {}
optimizacion_por_id = {}

for idx, group in df.groupby(columna_id):
    resultado_df = pd.DataFrame()

    for tickers_lista in group[columna_ticker]:
        for ticker in tickers_lista:
            # Elimina espacios de los tickers
            ticker = ticker.strip()

            url = f'https://www.marketwatch.com/investing/stock/{ticker}/download-data?mod=mw_quote_tab'
            #print(f"Obteniendo datos para {ticker} desde {url}")

            pagina = requests.get(url)

            # Selecciona la tabla con la clase específica
            sopa = BeautifulSoup(pagina.text, 'html.parser')
            tabla = sopa.find('div', class_="download-data")

            # Asegúrate de que la tabla fue encontrada antes de intentar leerla
            if tabla:
                df_ticker = pd.read_html(str(tabla))[0]

                # Elimina los símbolos de pesos de la columna 'Close' y conviértela a tipo numérico
                df_ticker['Close'] = pd.to_numeric(df_ticker['Close'].str.replace('[$,]', '', regex=True), errors='coerce')

                # Calcula los rendimientos con la nueva fórmula
                df_ticker['Rendimiento'] = (df_ticker['Close'].shift(1) - df_ticker['Close']) / df_ticker['Close']

                # Agrega los rendimientos al DataFrame final por ID
                resultado_df[ticker] = df_ticker['Rendimiento']

                #print(f"Rendimientos para {ticker} calculados correctamente.")
            else:
                print(f"No se encontró la tabla con la clase especificada para {ticker}.")

    # Calcula la covarianza entre los tickers y almacénala en el diccionario
    covarianza = resultado_df.cov()
    covarianza_por_id[idx] = covarianza

    # Calcula las estadísticas para cada ticker y almacénalas en el diccionario
    estadisticas = pd.DataFrame({
        'Media': resultado_df.mean(),
        'Varianza': resultado_df.var(),
        'DesviacionEstandar': resultado_df.std()
    })
    estadisticas_por_id[idx] = estadisticas.T  # Transponer el DataFrame

    # Agrega este DataFrame al diccionario
    resultados_por_id[idx] = resultado_df

    # Optimización de la cartera
    rendimientos = estadisticas['Media'].values
    covarianza_matrix = covarianza.values

    # Función objetivo a maximizar (rendimiento esperado)
    def objetivo(x):
        rendimiento_esperado = -np.dot(rendimientos, x)
        return rendimiento_esperado

    # Restricciones
    restricciones = ({'type': 'eq', 'fun': lambda x: np.sum(x) - 1},  # Suma de porcentajes igual a 100%
                     {'type': 'ineq', 'fun': lambda x: x},  # Porcentajes no negativos
                     {'type': 'ineq', 'fun': lambda x: 1 - x})  # Porcentajes no mayores a 100%

    # Límites de porcentajes (entre 0% y 100%)
    limites = tuple((0, 1) for _ in rendimientos)

    # Inicialización de pesos (podrías ajustar esto)
    pesos_iniciales = np.ones(len(rendimientos)) / len(rendimientos)

    # Resuelve el problema de optimización
    resultado_optimizacion = minimize(objetivo, pesos_iniciales, method='SLSQP', bounds=limites, constraints=restricciones)

    # Almacena los resultados de la optimización
    optimizacion_por_id[idx] = {
        'PesosOptimizados': resultado_optimizacion.x,
        'RendimientoOptimizado': -resultado_optimizacion.fun
    }

def obtener_tablas_por_id(user_id):
    covarianza_df = covarianza_por_id[user_id]
    estadisticas_df = estadisticas_por_id[user_id]
    optimizacion_df = optimizacion_por_id[user_id]

    # Convertir covarianza_df y estadisticas_df a DataFrames
    covarianza_df = pd.DataFrame(covarianza_df, index=estadisticas_df.columns, columns=estadisticas_df.columns)
    estadisticas_df = estadisticas_df.T

    # Convertir optimizacion_df a DataFrame
    optimizacion_df = pd.DataFrame(optimizacion_df).T

    return covarianza_df, estadisticas_df, optimizacion_df



"""# Muestra las tablas de covarianza
for idx, covarianza_df in covarianza_por_id.items():
    print(f"Tabla de Covarianza para ID {idx}:")
    print(covarianza_df)
    print("\n")

# Muestra las estadísticas
for idx, estadisticas_df in estadisticas_por_id.items():
    print(f"Estadísticas para ID {idx}:")
    print(estadisticas_df)
    print("\n")

# Muestra los resultados de la optimización
for idx, resultado_optimizacion in optimizacion_por_id.items():
    print(f"Resultados de la optimización para ID {idx}:")
    print("Pesos Optimizados:", resultado_optimizacion['PesosOptimizados'])
    print("Rendimiento Optimizado:", resultado_optimizacion['RendimientoOptimizado'])
    print("\n")
"""