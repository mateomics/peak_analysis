"""
peaks.py

Módulo para escribir las secuencias de unión en archivos FASTA separados, con salto de línea cada 80 nucleótidos,
según lo establecido en el formato FASTA. Esta función se utiliza para guardar las secuencias de forma que puedan
ser utilizadas con el software MEME en pasos posteriores.

Autor: Mateo Jiménez
Fecha: 2025-05-15
"""

import os

def write_fasta(peak_sequences, results_dir) -> None:
    """
    Escribe las secuencias de unión en archivos FASTA separados, con salto de línea cada 80 nucleótidos.

    Args:
        peak_sequences: Diccionario con las secuencias de unión.
    """
    for tf_name, sequences in peak_sequences.items(): # Iterar sobre cada TF y sus secuencias
        # Archivos FASTAs individuales
        with open(os.path.join(results_dir, f'{tf_name}.fa'), 'w') as output_file: # Un archivo por TF
            for index, sequence in enumerate(sequences):  # Sacar índice de cada pico
                output_file.write(f'>{tf_name}_peak_{index + 1}\n')
                for i in range(0, len(sequence), 80): # steps de 80 nucleótidos
                    output_file.write(f'{sequence[i:i + 80]}\n')
    
    print(f'Proceso completado. Se han escrito {len(peak_sequences)} archivos FASTA en el directorio de salida.')