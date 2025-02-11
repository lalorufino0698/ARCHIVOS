import os
import shutil
from datetime import datetime

# Ruta de la carpeta de origen y la carpeta de destino
ruta_origen = r'RUTA ORIGEN'
ruta_destino = r'RUTA DESTINO'

# Fecha de corte: 30 de enero de 2025
fecha_corte = datetime(2025, 1, 30)

def validar_rutas():
    # Verificar si la ruta de origen existe
    if not os.path.exists(ruta_origen):
        print(f"Error: La ruta de origen no existe o no es accesible: {ruta_origen}")
        return False
    
    # Verificar si la ruta de destino existe
    if not os.path.exists(ruta_destino):
        print(f"Error: La ruta de destino no existe o no es accesible: {ruta_destino}")
        return False
    
    return True

def copiar_archivos_sin_crear_carpetas():
    # Validar si las rutas de origen y destino son accesibles
    if not validar_rutas():
        return
    
    # Recorrer todas las carpetas en la ruta de origen
    for root, dirs, files in os.walk(ruta_origen):
        for archivo in files:
            # Ruta completa del archivo en la carpeta de origen
            ruta_archivo_origen = os.path.join(root, archivo)
            
            try:
                # Obtener la fecha de creación del archivo
                fecha_creacion = datetime.fromtimestamp(os.path.getctime(ruta_archivo_origen))
                
                # Verificar si el archivo es posterior a la fecha de corte
                if fecha_creacion >= fecha_corte:
                    # Obtener la ruta relativa del archivo
                    carpeta_relativa = os.path.relpath(root, ruta_origen)
                    ruta_carpeta_destino = os.path.join(ruta_destino, carpeta_relativa)

                    # Verificar si la carpeta ya existe en el destino
                    if os.path.exists(ruta_carpeta_destino):
                        ruta_archivo_destino = os.path.join(ruta_carpeta_destino, archivo)
                        
                        # Verificar si el archivo ya existe en el destino
                        if not os.path.exists(ruta_archivo_destino):
                            try:
                                # Copiar el archivo manteniendo su fecha de creación/modificación
                                shutil.copy2(ruta_archivo_origen, ruta_archivo_destino)
                                print(f"Archivo copiado: {ruta_archivo_destino}")
                            except Exception as e:
                                print(f"Error al copiar {archivo}: {e}")
                        else:
                            print(f"El archivo ya existe en el destino: {ruta_archivo_destino}")
                    else:
                        print(f"La carpeta destino no existe: {ruta_carpeta_destino}. No se copió {archivo}.")
                else:
                    print(f"Archivo no cumple con la fecha de corte: {ruta_archivo_origen}")
            
            except FileNotFoundError as e:
                print(f"Error al acceder a la fecha de creación del archivo {archivo}: {e}. Se saltará este archivo.")
            except Exception as e:
                print(f"Error inesperado con el archivo {archivo}: {e}")

# Ejecutar la función
copiar_archivos_sin_crear_carpetas()
