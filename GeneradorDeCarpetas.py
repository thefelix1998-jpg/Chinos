import os
import shutil
import streamlit as st

st.title("Generador de Carpetas con Descarga ZIP")

# Entradas del usuario
cantidad = st.number_input("Número de carpetas a crear:", min_value=1, step=1)
nombre = st.text_input("Nombre base de las carpetas (puede dejarlo vacío):")

# Botón para ejecutar
if st.button("Crear carpetas"):
    # Crear directorio temporal dentro del proyecto
    ruta = "carpetas_generadas"
    os.makedirs(ruta, exist_ok=True)

    # Crear las carpetas
    for i in range(1, cantidad + 1):
        if nombre.strip():
            carpeta = os.path.join(ruta, f"{nombre} {i}")
        else:
            carpeta = os.path.join(ruta, str(i))
        os.makedirs(carpeta, exist_ok=True)

    # Crear archivo ZIP
    zip_path = "carpetas_generadas.zip"
    shutil.make_archive("carpetas_generadas", 'zip', ruta)

    # Mostrar mensaje y botón de descarga
    if nombre.strip():
        st.success(f"✅ Se han creado {cantidad} carpetas con el nombre '{nombre}'")
    else:
        st.success(f"✅ Se han creado {cantidad} carpetas numeradas")

    with open(zip_path, "rb") as f:
        st.download_button("📥 Descargar carpetas en ZIP", f, file_name=zip_path)
