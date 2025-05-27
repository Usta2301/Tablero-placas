import pandas as pd

def cargar_placas_permitidas(ruta_excel="PlacasPermitidas.xlsx"):
    df = pd.read_excel(ruta_excel)
    return df['Placa'].tolist()

def verificar_acceso(placa, lista_autorizada):
    return "ACCESO PERMITIDO" if placa in lista_autorizada else "ACCESO DENEGADO"
