import pandas as pd

# Archivos de entrada
archivos_excel = {
    "import_2024": "IMPORTACION-HIDROCARBUROS-VOLUMEN-2024-12.xlsx",
    "import_2025": "IMPORTACION-HIDROCARBUROS-VOLUMEN-2025-05.xlsx",
}

# Convertir a CSV con encabezados correctos
for nombre, ruta in archivos_excel.items():
    df = pd.read_excel(ruta, header=6)  # La fila 7 (índice 6) contiene los encabezados correctos
    df.to_csv(f"{nombre}.csv", index=False)
    print(f"{ruta} convertido correctamente a {nombre}.csv")
