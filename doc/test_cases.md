### Casos de Prueba para el Módulo 1: Extractor y Creador de Secuencias FASTA


1.  **Caso: Archivo del genoma no se encuentra.**
    
    -   **Entradas:**
        -   Ruta incorrecta o inexistente para el archivo FASTA del genoma.
        -   Archivo de picos válido.
        -   Directorio de salida.
    -   **Esperado:** `"Error: Genome file not found"`
    
    ```python
    mk_fasta_from_peaks.py -i peak_file.txt -g Ecoli.fna -o fasta_peaks/ 
    ```
    ```
    Error: "Ecoli.fna" genome file not found
    ```
 
  ---
2.  **Caso: Archivo de genomas (FASTA) vacío.**
    
    -   **Entradas:**
        -   Archivo de picos.
        -   Archivo FASTA del genoma vacío.
        -   Directorio de salida.
    -   **Esperado:** `"Error: the genome file is empty or uncomplete."`

 ```python
    mk_fasta_from_peaks.py -i peak_file.txt -g Ecoli.fna -o fasta_peaks/ 
```
  
```
Error: the peak file is empty
``` 
---
3.  **Caso: Archivo de picos vacío.**
    
    -   **Entradas:**
        -   Archivo de picos vacío.
        -   Archivo FASTA del genoma.
        -   Directorio de salida.
    -   **Esperado:** `"Error: the peak file is empty."`

 ```python
    mk_fasta_from_peaks.py -i peak_file.txt -g Ecoli.fna -o fasta_peaks/ 
```
  
```
Error: the peak file is empty
```
---
4.  **Caso: Posiciones `Peak_start` y `Peak_end` fuera del rango del genoma.**
    
    -   **Entradas:**
        -   Archivo de picos con algunas posiciones `Peak_start` y `Peak_end` fuera del tamaño del genoma.
        -   Archivo FASTA del genoma válido.
        -   Directorio de salida.
    -   **Esperado:**
        -   El sistema debe imprimir un mensaje de advertencia: `"Warning: Some peaks are bigger than the genome". Check the log.out file`
        
        -   Generar un archivo de log indicando los picos fuera de rango. El archivo debe contener las líneas del archivo de picos que tienen problemas.

```python
    mk_fasta_from_peaks.py -i peak_file.txt -g Ecoli.fna -o fasta_peaks/ 
```

```bash
ls
```

```bash
log.out
fasta_peaks/
```
---
5.  **Caso: Directorio inexistente.**
    
    -   **Entradas:**
        -   Archivo de picos.
        -   Archivo FASTA del genoma.
        -   Directorio de salida inexistente.
    -   **Esperado:** `"Error: the path does not exist."`

 ```python
    mk_fasta_from_peaks.py -i peak_file.txt -g Ecoli.fna -o fasta_peaks/ 
```
  
```
Error: the path does not exist
```
---
6.  **Caso: Parámetros omitidos.**
    
    -   **Entradas:**
        -   Archivo de picos.
        -   Archivo FASTA del genoma.
		---
		-   Archivo de picos.
        -   Directorio de salida.
		---
        -   Archivo FASTA del genoma.
        -   Directorio de salida.
		
    -   **Esperado:** `"Error: missing arguments."`

 ```python
    mk_fasta_from_peaks.py -i peak_file.txt -g Ecoli.fna -o fasta_peaks/ 
```
  
```
Error: missing arguments
```
---
7.  **Caso: Start más grande que End.**
    
    -   **Entradas:**
        -   Archivo de picos cambiados (lectura backward).
        -   Archivo FASTA del genoma.
        -   Directorio de salida.
		
    -   **Esperado:** `"Error: negative difference between peaks."`

 ```python
    mk_fasta_from_peaks.py -i peak_file.txt -g Ecoli.fna -o fasta_peaks/ 
```
  
```
Error: negative difference between peaks
```
---