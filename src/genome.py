"""
genome.py

Módulo para leer y analizar los archivos FASTA y TSV para determinar las secuencias de unión de picos.

Autor: Mateo Jiménez
Fecha: 2025-05-15
"""

import re

def peak_binding_sites(fasta_file, tsv_file):
        """
        Busca y devuelve los sitios de unión de picos en el archivo FASTA con base en el archivo tsv.

        Returns:
            dict: TF name como key y secuencia de unión como value.
        """
        fasta_sequence = '' # string para almacenar la secuencia completa de corrido
        peak_sequences = {} # diccionario para almacenar las secuencias de unión

        with open(fasta_file, 'r') as fasta_file:
            for line in fasta_file:
                if not line.startswith('>'):
                    fasta_sequence += line.strip().upper()

        with open(tsv_file, 'r') as tsv_file:
            for line in tsv_file:
                if re.match(r'^\s+\w*[a-zA-Z]\w*', line): # Si no es Header
                    continue
                line = line.split('\t')
                tf_name, peak_start, peak_end = line[2], int(float(line[3])), int(float(line[4])) # porque tienen decimal

                if peak_start > peak_end:
                    print(f'Error: el inicio del pico ({peak_start}) es mayor que el final ({peak_end}).\nSaltando...')
                    continue
                peak_sequence = fasta_sequence[peak_start:peak_end + 1] # +1 porque el slice no incluye el último índice

                if tf_name in peak_sequences: # Si ya existe el TF en el diccionario
                    peak_sequences[tf_name].append(peak_sequence)
                else:
                    peak_sequences[tf_name] = [peak_sequence]
        
            return peak_sequences
