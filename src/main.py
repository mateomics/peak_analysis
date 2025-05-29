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

from args import parse_args
from check_fasta import check_fasta_file
from check_tsv import check_tsv_file
from genome import peak_binding_sites
from peaks import write_fasta

def main() -> None:
    """
    Función principal del script.
    Ejecuta el análisis del archivo FASTA y extrae sus secuencias de unión
    en distintos archivos FASTA individuales mediante el uso de módulos auxiliares.
    """

    # Archivos de entrada y directorio de salida
    args = parse_args()

    fasta_file = os.path.normpath(args.fasta_file)
    tsv_file = os.path.normpath(args.tsv_file)
    output_dir = os.path.normpath(args.output_dir)

    validado = True # Bandera para verificar si los archivos y directorio de salida son válidos

    # Verificación de existencia del archivo FASTA
    fasta_file_score = check_fasta_file(fasta_file)
    if fasta_file_score < 3:
        print(f'\nEl archivo pasó {fasta_file_score}/3 validaciones. Intente de nuevo.\n')
        validado = False

    # Verificación de existencia del archivo TSV
    tsv_file_score = check_tsv_file(tsv_file)
    if tsv_file_score < 3:
        print(f'\nEl archivo pasó {tsv_file_score}/3 validaciones. Intente de nuevo.\n')
        validado = False

    # Verificación de existencia del directorio de salida
    if not os.path.isdir(output_dir):
        print(f'El directorio de salida "{output_dir}" no existe. Intente de nuevo.\n')
        validado = False

    if not validado:
        sys.exit(1)  # Si alguna validación falla, el programa no puede continuar

    print('Archivos y directorio de salida correctamente validados. Procediendo a buscar los picos de unión...\n')

    # Extracción de secuencias de unión
    peak_sequences = peak_binding_sites(fasta_file, tsv_file)

    # Escritura de los distintos FASTA separados
    write_fasta(peak_sequences, output_dir)

if __name__ == '__main__':
    main()
