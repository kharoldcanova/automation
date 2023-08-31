import os
import shutil

# Letra asignada a tu USB en Windows (por ejemplo, "E:\\")
letra_usb = "F:\\"

# Ruta de la carpeta "backup" en tu USB
backupDir = os.path.join(letra_usb, "backup")

# Verificar si la carpeta "backup" existe
if os.path.exists(backupDir):
    print("La carpeta ya existe.")
    shutil.rmtree(backupDir)
else:
    os.mkdir(backupDir)
    print("Carpeta 'backup' creada.")

# Definir ruta de respaldo
ruta_destino = backupDir

# Un arreglo de rutas originales
rutas_originales = [
    "E:\\KHAROLD\\Example",

]

# Recorrer el arreglo de rutas originales
for ruta_original in rutas_originales:
    print(f"Se iniciará la copia de {ruta_original} en breves instantes...")
    shutil.copytree(ruta_original, os.path.join(ruta_destino, os.path.basename(ruta_original)))
    print(f"Copiando contenido de {ruta_original} al USB en la carpeta 'backup'... ¡Hecho!")
