import argparse
import os
from paths import DATA_DIR, RESULTS_DIR

def parse_args() -> argparse.Namespace:
    """
    Función para analizar los argumentos de la línea de comandos que especifican 
    los archivos de entrada y salida para el análisis de secuencias de unión en archivos FASTA.
    Args:
        None
    Returns:
        argparse.Namespace: Objeto con los argumentos analizados.
    """
    # Definición del parser de argumentos
    parser = argparse.ArgumentParser(
        description='Análisis de secuencias de unión en archivos FASTA, dado un TSV.'
    )
    
    parser.add_argument(
        '-fa', '--fasta_file',
        type=str,
        default=os.path.join(DATA_DIR, 'E_coli_K12_MG1655_U00096.3.txt'), # No se establece un required porque se toma uno por default
        metavar='FASTA',
        help='Ruta al archivo FASTA que contiene las secuencias genómicas.Por defecto: E_coli_K12_MG1655_U00096.3.txt en el directorio de datos.'
    )

    parser.add_argument(
        '-tsv', '--tsv_file',
        type=str,
        default=os.path.join(DATA_DIR, 'union_peaks_file.tsv'),
        metavar='TSV',
        help='Ruta al archivo TSV que contiene los picos de unión.Por defecto: union_peaks_file.tsv en el directorio de datos.'
    )

    parser.add_argument(
        '-o', '--output_dir',
        type=str,
        default=RESULTS_DIR,
        metavar='OUTPUT',
        help='Ruta al directorio donde se guardarán los resultados.Por defecto: results en el directorio del proyecto.'
    )

    return parser.parse_args()