import easyocr

reader = easyocr.Reader(['es'])

def reconocer_placa(imagen_path):
    resultados = reader.readtext(imagen_path)
    for _, texto, _ in resultados:
        placa = texto.upper().replace(" ", "")
        if len(placa) >= 6:
            return placa[:3] + " " + placa[3:]
    return None
