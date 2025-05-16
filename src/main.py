"""
main.py

Módulo principal para ejecutar el análisis de un archivo FASTA y extraer secuencias de unión 
mediante la importación de módulos auxiliares en el proyecto.
Aquí se especifican los archivos de entrada.

Autor: Mateo Jiménez
Fecha: 2025-05-15
"""
import sys
import os

from paths import DATA_DIR, RESULTS_DIR
from check_fasta import check_fasta_file
from genome import peak_binding_sites
from peaks import write_fasta

# Archivos de entrada
fasta_file = os.path.normpath(os.path.join(DATA_DIR, 'E_coli_K12_MG1655_U00096.3.fa'))
tsv_file = os.path.normpath(os.path.join(DATA_DIR, 'union_peaks_file.tsv'))

# Verificación de existencia del archivo FASTA
fasta_file_score = check_fasta_file(fasta_file)

if fasta_file_score < 3:
    print(f'\nEl archivo pasó {fasta_file_score}/3 validaciones. Intente de nuevo.\n')
    sys.exit(1)

# Verificación de existencia del directorio de salida
if not os.path.isdir(RESULTS_DIR):
    print(f'El directorio de salida "{RESULTS_DIR}" no existe. Intente de nuevo.\n')
    sys.exit(1)

print('Archivo y directorio de salida correctamente validados. Procediendo a buscar los picos de unión...\n')

# Extracción de secuencias de unión
peak_sequences = peak_binding_sites(fasta_file, tsv_file)

# Escritura de los distintos FASTA separados
write_fasta(peak_sequences, RESULTS_DIR)
