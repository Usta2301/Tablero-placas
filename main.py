import cv2
from reconocimiento import reconocer_placa
from verificador import cargar_placas_permitidas, verificar_acceso
from pantalla import mostrar_mensaje

def capturar_imagen(nombre_archivo="captura.jpg"):
    cam = cv2.VideoCapture(0)
    ret, frame = cam.read()
    if ret:
        cv2.imwrite(nombre_archivo, frame)
        return nombre_archivo
    else:
        print("Error al capturar imagen")
        return None

def main():
    imagen = capturar_imagen()
    if imagen:
        placa_detectada = reconocer_placa(imagen)
        if placa_detectada:
            lista = cargar_placas_permitidas()
            estado = verificar_acceso(placa_detectada, lista)
            mostrar_mensaje(f"{placa_detectada} - {estado}")
        else:
            mostrar_mensaje("No se detectó una placa válida")

if __name__ == "__main__":
    main()
