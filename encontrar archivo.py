import os

def obtener_ultimos_archivos_modificados(ruta, cantidad=10):
    # Lista para almacenar información de los archivos
    archivos_modificados = []

    # Recorrer la ruta especificada y sus subdirectorios
    for carpeta_actual, subcarpetas, archivos in os.walk(ruta):
        # Iterar sobre cada archivo en la carpeta actual
        for nombre_archivo in archivos:
            ruta_completa = os.path.join(carpeta_actual, nombre_archivo)
            # Obtener la fecha de la última modificación del archivo actual
            fecha_modificacion = os.path.getmtime(ruta_completa)
            # Agregar la información del archivo a la lista
            archivos_modificados.append((ruta_completa, fecha_modificacion))

    # Ordenar la lista de archivos por fecha de modificación (en orden descendente)
    archivos_modificados.sort(key=lambda x: x[1], reverse=True)

    # Retornar los últimos 'cantidad' archivos modificados
    return archivos_modificados[:cantidad]

# Ruta de la carpeta que deseas examinar
ruta_carpeta = 'C:\\Users\\ken\\Documents\\StarCraft II'


# Obtener los últimos 10 archivos modificados
ultimos_archivos_modificados = obtener_ultimos_archivos_modificados(ruta_carpeta)

# Mostrar los últimos 10 archivos modificados con sus fechas
print("Últimos 10 archivos modificados:")
for archivo, fecha_modificacion in ultimos_archivos_modificados:
    print(f"Archivo: {archivo} - Fecha de modificación: {fecha_modificacion}")
