"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta.
"""

# pylint: disable=import-outside-toplevel
import pandas as pd

def pregunta_01():
    """
    Construya y retorne un dataframe de Pandas a partir del archivo
    'files/input/clusters_report.txt'. Los requierimientos son los siguientes:

    - El dataframe tiene la misma estructura que el archivo original.
    - Los nombres de las columnas deben ser en minusculas, reemplazando los
      espacios por guiones bajos.
    - Las palabras clave deben estar separadas por coma y con un solo
      espacio entre palabra y palabra.


    """
    filename = "files/input/clusters_report.txt"
    
    with open(filename, 'r', encoding='utf-8') as file:
        lines = file.readlines()[4:]

    clusters = []
    temp_cluster = []

    for line in lines:
        line = line.strip()

        if line:
            parts = line.split()
            if not temp_cluster:
                temp_cluster = [
                    int(parts[0]),
                    int(parts[1]),
                    float(parts[2].replace(',', '.')),
                    " ".join(parts[4:])
                ]
            else:
                temp_cluster[3] += " " + " ".join(parts)
        else:
            if temp_cluster:
                temp_cluster[3] = temp_cluster[3].replace('.', '')
                clusters.append(temp_cluster)
                temp_cluster = []

    if temp_cluster:
        temp_cluster[3] = temp_cluster[3].replace('.', '')
        clusters.append(temp_cluster)

    return pd.DataFrame(clusters, columns=['cluster', 'cantidad_de_palabras_clave', 'porcentaje_de_palabras_clave', 'principales_palabras_clave'])
