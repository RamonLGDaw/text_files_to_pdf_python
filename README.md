# Generación de PDF a partir de Archivos de Texto con FPDF

Este proyecto utiliza la biblioteca FPDF para generar archivos PDF a partir de varios archivos de texto. El script recorre todos los archivos `.txt` en la carpeta `Text+Files`, extrae su contenido y crea un documento PDF para cada archivo. Cada archivo de texto se convierte en una página dentro del PDF, con el nombre del archivo como título y el contenido del archivo como texto.

### Funcionalidades:
- **Lectura de archivos de texto**: El script recorre todos los archivos de texto en un directorio específico.
- **Generación de PDF**: Crea un archivo PDF en formato A4, con cada archivo de texto en una nueva página.
- **Formato personalizable**: El título del archivo se agrega como encabezado en negrita y el contenido se muestra en texto justificado.

Este proyecto es útil para automatizar la conversión de documentos de texto a PDF, especialmente para la recopilación de información o la creación de informes en formato PDF.

Los archivos PDF generados se guardan en la carpeta `PDF's`, con un nombre de archivo predefinido (`Animals.pdf`).
