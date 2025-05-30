"""
check_tsv.py

Módulo para validar el archivo TSV dado y su contenido.

Autor: Mateo Jiménez
Fecha: 2025-05-29
"""

import os
import re

def check_tsv_file(tsv_file) -> int:
    """
    Verifica la existencia y extensión del archivo TSV. Llama a check_tsv_content() para validar el contenido.
    Args:
        tsv_file (str): Ruta del archivo TSV a verificar-
    Returns:
        int: Score del archivo basado en las validaciones.
    """
    file_score = 0  # Inicializa el score del archivo
    message = f'El archivo {tsv_file}'

    print('\t')
    if not os.path.isfile(tsv_file):  # Verifica si el archivo existe
        print(f'{message} no existe.')
        return file_score  # Si no existe, retorna 0 porque ni siquiera existe
    print(f'{message} existe.')
    file_score += 1

    if not re.search(r'\.tsv$', tsv_file):  # Verifica si tiene la extensión .tsv
        print(f'{message} no cuenta con una extensión válida (.tsv).')
    else:
        print(f'{message} cuenta con una extensión válida.')
        file_score += 1

    # Verificar el contenido del archivo
    if not check_tsv_content(tsv_file):
        print(f'{message} no tiene un formato TSV válido.')
    else:
        print(f'{message} tiene un formato TSV válido.')
        file_score += 1

    return file_score

def check_tsv_content(tsv_file) -> bool:
    """
    Verifica el contenido del archivo TSV para asegurarse de que tiene un formato válido.
    Args:
        tsv_file (str): Ruta del archivo TSV a verificar.
    Returns:
        bool: True si el contenido es válido, False en caso contrario.
    """

    REQUIRED_COLUMNS = {'TF_name', 'Peak_start', 'Peak_end'} # Set de columnas que deben estar presentes para el análisis

    with open(tsv_file, 'r') as file:  # newline='' evita problemas con saltos de línea en diferentes sistemas operativos
        header = file.readline().strip().split('\t') # Lee la primera línea y la divide por tabulaciones

    if not REQUIRED_COLUMNS.issubset(header):
        print(f'Error: El archivo debe tener los encabezados {", ".join(REQUIRED_COLUMNS)}.')
        return False
    
    return True  # Si todas las columnas requeridas están presentes