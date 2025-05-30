"""
genome.py

Módulo para leer y analizar los archivos FASTA y TSV para determinar las secuencias de unión de picos.

Autor: Mateo Jiménez
Fecha: 2025-05-15
"""

import pandas as pd

def peak_binding_sites(fasta_file, tsv_file) -> dict:
    """
    Extrae las secuencias de unión de picos desde un archivo FASTA con base en un TSV.
    Utiliza dataframes de pandas para manejar los datos de manera eficiente al hacer operaciones
    de filtrado y agrupamiento de forma vectorizada.
    Args:
        fasta_file (str): Ruta del archivo FASTA que contiene la secuencia del genoma.
        tsv_file (str): Ruta del archivo TSV que contiene los picos y sus posiciones.
    Returns:
        dict: Diccionario con las secuencias de unión agrupadas por nombre de factor de transcripción (TF_name).
    """
    peak_sequences = {} # diccionario para almacenar las secuencias de unión

    # Leer archivo FASTA
    with open(fasta_file, 'r') as fasta_file: # Abrir archivo FASTA en modo lectura
        fasta_sequence = ''.join(line.strip().upper() for line in fasta_file if not line.startswith('>')) # Ignorar encabezados y líneas vacías

    genome_length = len(fasta_sequence)

    # Leer archivo TSV
    df = pd.read_csv(tsv_file, sep='\t', comment='#', header=0, usecols=['TF_name', 'Peak_start', 'Peak_end']) # Ignora comentarios y hace explícito el header

    # Convertir a enteros
    df['Peak_start'] = df['Peak_start'].astype(float).astype(int)
    df['Peak_end'] = df['Peak_end'].astype(float).astype(int)

    # Filtrar picos válidos
    invalid_peaks = df[df['Peak_start'] > df['Peak_end']]
    if not invalid_peaks.empty:
        print(f"{len(invalid_peaks)} picos tienen Peak_start > Peak_end. Serán descartados del análisis.")

    df = df[
        (df['Peak_start'] >= 0) & # Starts positivos
        (df['Peak_end'] < genome_length) & # Ends dentro del genoma del FASTA
        (df['Peak_start'] <= df['Peak_end']) # No picos con inicio mayor que el final
        ]
    
    df.columns = df.columns.str.strip() # Quita espacios en los nombres por cualquier cosa

    # Verificar si hay picos válidos
    if df.empty:
        print("No se encontraron picos válidos en el archivo TSV. Asegúrese de que los picos estén dentro del rango del genoma.")
        return peak_sequences  # Retorna un diccionario vacío si no hay picos válidos

    # Extraer secuencias de unión
    df['sequence'] = df.apply(
        lambda row: fasta_sequence[row['Peak_start']:row['Peak_end'] + 1], # Slice para cada fila
        axis=1 # Sobre cada fila, no columna
    )

    # Agrupar con key TF_name, value lista de secuencias
    peak_sequences = df.groupby('TF_name')['sequence'].apply(list).to_dict() # Secuencias agrupadas por TF_name en listas

    return peak_sequences