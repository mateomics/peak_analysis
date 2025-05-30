# Proyecto de Automatización para la Extracción de Sitios de Unión de Factores de Transcripción en E. coli en experimentos de ChIP-Seq

## Resumen

Este proyecto tiene como objetivo automatizar el proceso de identificación del sitio exacto de unión de los reguladores transcripcionales para 144 factores de transcripción (TFs) en el genoma completo de *Escherichia coli*. Las regiones de unión de estos TFs se han determinado mediante la técnica ChIP-seq.

## Datos Disponibles

### Archivo de Picos
> union_peaks_file.tsv

Contiene información sobre las regiones de unión de los 144 factores de transcripción. Se organiza en las siguientes columnas:

- **Dataset_Ids**: Identificadores de los datasets. Cada identificador representa un experimento o condición específica bajo la cual se identificaron los sitios de unión para el TF correspondiente.
- **TF_name**: Nombre del factor de transcripción que se une a la secuencia de ADN especificada.
- **Peak_start**: Posición inicial del pico de unión en el genoma.
- **Peak_end**: Posición final del pico de unión en el genoma.
- **Peak_center**: Posición central del pico de unión en el genoma.
- **Peak_number**: Número secuencial del pico, útil para referencias internas dentro del mismo conjunto de datos.
- **Max_Fold_Enrichment**: Enriquecimiento máximo observado en el pico.
- **Max_Norm_Fold_Enrichment**: Enriquecimiento máximo normalizado.
- **Proximal_genes**: Genes próximos al sitio de unión.
- **Center_position_type**: Tipo de posición central del pico (por ejemplo, intergénica, intrónica, etc.).

### Genoma Completo de E. coli
Disponible en formato FASTA.
> E_coli_K12_MG1655_U00096.3.txt

## Objetivos del Proyecto

### Generación de Archivos FASTA
Desarrollar un programa que extraiga y compile las secuencias de picos para cada TF en archivos individuales en formato FASTA. Cada archivo representará un regulador específico.

## Buenas Prácticas de Desarrollo

Para asegurar la calidad y mantenibilidad del software, el proyecto seguirá estas buenas prácticas:

- **Control de Versiones**: Uso de Git para el control de versiones, asegurando una gestión eficaz de los cambios y la colaboración.
- **Revisión de Código**: Implementación de revisiones de código periódicas para mejorar la calidad del software y compartir conocimientos entre el equipo.
- **Documentación Exhaustiva**: Mantener una documentación completa tanto del código como de los procesos operativos, asegurando que cualquier nuevo colaborador pueda integrarse fácilmente.
- **Pruebas Automatizadas**: Desarrollo de pruebas automatizadas para validar la funcionalidad y robustez del software.

## Plan de Implementación

1. **Desarrollo del Extractor de Secuencias**: Programación de la tarea que consiste en generar los archivos FASTA a partir del archivo de picos. Como es un proceso automatizado, todos la información requerida para ejecutar los programas debe ser por línea de comandos.
2. **Integración y Pruebas**: Combinación de los módulos desarrollados y realización de pruebas integrales para asegurar la funcionalidad.
3. **Implementación de la librería Argparse**: Manejo de argumentos con la librería, usando argumentos opcionales para indicar las rutas de los archivos de input y del directorio de output.
```
	- usage: main.py [-h] [-fa FASTA] [-tsv TSV] [-o OUTPUT]

Análisis de secuencias de unión en archivos FASTA, dado un TSV.

options:
  -h, --help            show this help message and exit
  -fa FASTA, --fasta_file FASTA
                        Ruta al archivo FASTA que contiene las secuencias genómicas.Por defecto: E_coli_K12_MG1655_U00096.3.txt en el directorio de datos.
  -tsv TSV, --tsv_file TSV
                        Ruta al archivo TSV que contiene los picos de unión.Por defecto: union_peaks_file.tsv en el directorio de datos.
  -o OUTPUT, --output_dir OUTPUT
                        Ruta al directorio donde se guardarán los resultados.Por defecto: results en el directorio del proyecto.
                        
```
                        
4. **Validación de errores por formato o extensión de los archivos**: Usar *dataframes*, *ifs*, *RegEx*


NOTA: Creo que podrias cambiar un poco el orden de los pasos o como de la informacion, me refiero a en lugar de escribir lo de como usar el main en esta parte de argparse, podrias agregarlo como otro punto para que sea un poco mas legible, pero en general creo que todo lo demas esta bien
