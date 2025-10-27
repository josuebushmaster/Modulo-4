# Módulo 4 — instrucciones rápidas

Pasos mínimos para levantar el proyecto en Windows (PowerShell):

1) Abrir PowerShell y situarse en la raíz del proyecto:

```powershell
Set-Location -Path "C:\PERSONAL\UMA\Modulo 4"
```

2) Crear (si no existe) y activar el entorno virtual `.venv`:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

Si PowerShell bloquea la activación:

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
.\.venv\Scripts\Activate.ps1
```

3) Instalar dependencias:

```powershell
python -m pip install --upgrade pip
python -m pip install -r .\requirements.txt
python -m pip install openpyxl    # para leer/escribir .xlsx
# Opcional: python -m pip install pyqt5   # si quieres que matplotlib abra ventanas
```

4) Ejecutar los scripts (ejemplos):

```powershell
python .\"clase 4\ejercicio1.py"     # demo pandas
python .\"clase 4\ejercicio2.py"     # lee Facturacion.csv
python .\"clase 5\ejericicio1-1.py"  # predicción Titanic (usa archivos en clase 5)
python .\"clase 5\actividad3.py"     # clustering (si no hay GUI guarda PNG)
```

5) Configurar VSCode (opcional): seleccionar el intérprete del venv (`.venv\Scripts\python.exe`) en la paleta de comandos o crear `.vscode/settings.json` con:

```json
{
	"python.defaultInterpreterPath": "${workspaceFolder}\\.venv\\Scripts\\python.exe"
}
```

Notas breves:
- Los scripts fueron ajustados para buscar archivos de datos relativos a la carpeta donde están los scripts (evita FileNotFoundError cuando el CWD es distinto).
- Si matplotlib da error relacionado con Tcl/Tk, instala `pyqt5` o crea el venv con una instalación de Python que incluya Tcl/Tk.
- Actualiza `requirements.txt` desde tu venv con `python -m pip freeze > requirements.txt` una vez que tengas todo instalado.

Listo: con estos pasos tendrás el proyecto listo para ejecutar los ejemplos.

