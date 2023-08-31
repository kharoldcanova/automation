import os
import shutil

# Letra asignada a tu USB en Windows (por ejemplo, "F:\\")
letra_usb = "F:\\"

# Ruta de la carpeta "backup" en tu USB
backupDir = os.path.join(letra_usb, "backup")

# Definir rutas de origen
rutas_origen = [
    "E:\\KHAROLD\\Backup",  # Ruta a la carpeta original
]

# Verificar si la carpeta de respaldo existe en el USB
if os.path.exists(backupDir):
    # Recorrer los elementos dentro de la carpeta de respaldo
    for elemento in os.listdir(backupDir):
        ruta_elemento_backup = os.path.join(backupDir, elemento)
        if os.path.isdir(ruta_elemento_backup):
            for ruta_origen in rutas_origen:
                # Crear la carpeta en la ruta de origen si no existe
                ruta_destino = os.path.join(ruta_origen, elemento)
                if not os.path.exists(ruta_destino):
                    os.makedirs(ruta_destino)
                # Copiar el contenido desde la carpeta de respaldo a la ruta de origen
                ruta_destino = os.path.join(ruta_origen, elemento)
                shutil.copytree(ruta_elemento_backup, ruta_destino, dirs_exist_ok=True)
                print(f"Contenido de {elemento} restaurado en {ruta_destino}")
else:
    print("La carpeta de respaldo no existe en el USB.")
