"""
check_fasta.py

Módulo para validar los archivos FASTA y su contenido. Incluye funciones para verificar la existencia del
mismo, su extensión y el formato en el que están, asignando un score e inforamando al usuario de los errores.

Autor: Mateo Jiménez
Fecha: 2025-05-15
"""

import os
import re

def check_fasta_file(fasta_file): # Validar la existencia del archivo y directorio
    """
    Verifica existencia y extensión del archivo FASTA. Llama a check_fasta_content() para validar el contenido.

    Returns:
        bool: True si pasa todas las pruebas, False en caso contrario.
    """
    file_score = 0 # Inicializa el score del archivo
    message = f'El archivo {fasta_file}'

    if not os.path.isfile(fasta_file): # Módulo de os para verificaciones del archivo
        print(f'{message} no existe.')
        return file_score # Si no existe, retorna 0 porque ni siquiera existe
    print(f'{message} existe.')
    file_score += 1
        
    if not re.search(r'\.(fasta|fa|fna|txt)$', fasta_file): # Si tiene una extensión válida (incluyendo txt). 'r' de raw para usar regex
        print(f'{message} no cuenta con una extensión válida (.txt, .fna, .fasta o .fa).')
    else:
        print(f'{message} cuenta con una extensión válida.')
        file_score += 1
        
    # Verificar el contenido del archivo
    if not check_fasta_content(fasta_file):
        print(f'{message} no tiene un formato FASTA válido.')
    else:
        print(f'{message} tiene un formato FASTA válido.')
        file_score += 1
        
    return file_score


def check_fasta_content(fasta_file):
    """
    Verifica el contenido del archivo FASTA para asegurarse de que tiene un formato válido.

    Returns:
        bool: True si el contenido es válido, False en caso contrario.
    """
    with open(fasta_file, 'r') as file: # Modo de lectura
        first_line = file.readline().strip()
            
    if not first_line.startswith(">"): # Si la línea es el encabezado ('>')
        return False
    return True # caso en el que sí lo es