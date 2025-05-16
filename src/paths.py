"""
paths.py

Módulo para definir las rutas relativas al directorio del módulo, incluyendo
los directorios 'data' y 'results' del proyecto. Útil para análisis de archivos FASTA
y extracción de secuencias de unión.

Autor: Mateo Jiménez
Fecha: 2025-05-15
"""

import os

# Directorio del módulo
SRC_DIR = os.path.dirname(os.path.abspath(__file__))

# Directorios de datos y resultados
DATA_DIR = os.path.normpath(os.path.join(SRC_DIR, '../data'))
RESULTS_DIR = os.path.normpath(os.path.join(SRC_DIR, '../results'))

