# Smart Weather Station AI Lab — Hoja de resumen del entorno de trabajo

## 1. Objetivo de lo que hemos hecho / 10-06-2026

Hemos preparado el entorno inicial de desarrollo para el proyecto:

**Smart Weather Station AI Lab**

Este proyecto será el hilo conductor del roadmap **Máster IA — Preparación 2026-2028**.

La idea es construir una estación meteorológica con sensores reales y material reciclado, y usar sus datos para aprender:

* Python para IA
* NumPy
* pandas
* matplotlib
* Jupyter
* Git y GitHub
* Machine Learning
* Edge AI
* Embedded systems
* Documentación técnica

---

## 2. Herramientas instaladas o configuradas

### Herramientas principales

* Python 3.12
* Git
* Visual Studio Code
* PowerShell
* JupyterLab
* NumPy
* pandas
* matplotlib
* pytest
* ruff

### Extensiones recomendadas en VS Code

* Python — Microsoft
* Pylance — Microsoft
* Jupyter — Microsoft

---

## 3. Comandos iniciales de comprobación

Estos comandos sirven para comprobar si las herramientas están instaladas:

```powershell
py --version
git --version
code --version
```

En mi caso:

```text
py --version        → Python 3.12.0
git --version       → Git 2.54.0
code --version      → VS Code instalado
```

Nota: en este equipo `python` no funcionaba inicialmente, pero `py` sí. Por eso hemos usado `py`.

---

## 4. Crear carpeta del proyecto

Desde PowerShell:

```powershell
cd $HOME\Documents
mkdir AI-Master-2026-2028
cd AI-Master-2026-2028
mkdir smart-weather-station-ai-lab
cd smart-weather-station-ai-lab
code .
```

Esto crea la carpeta del proyecto y la abre en VS Code.

---

## 5. Crear entorno virtual

Dentro de la carpeta del proyecto:

```powershell
py -m venv .venv
```

Activar el entorno virtual:

```powershell
.\.venv\Scripts\Activate.ps1
```

Cuando está activo, aparece algo así:

```powershell
(.venv) PS C:\Users\...\smart-weather-station-ai-lab>
```

Si PowerShell da problemas, alternativa:

```powershell
.venv\Scripts\activate.bat
```

---

## 6. Instalar librerías principales

Con `.venv` activado:

```powershell
py -m pip install --upgrade pip
py -m pip install numpy pandas matplotlib jupyterlab ipykernel pytest ruff
```

Comprobar librerías instaladas:

```powershell
py -m pip list
```

Guardar dependencias exactas:

```powershell
py -m pip freeze > requirements.txt
```

---

## 7. Estructura inicial del proyecto

La estructura inicial del proyecto quedó así:

```text
smart-weather-station-ai-lab/
│
├── .venv/
├── .vscode/
│   └── settings.json
│
├── data/
├── docs/
│   ├── architecture.md
│   ├── hardware.md
│   └── project_log.md
│
├── firmware/
├── images/
├── notebooks/
│   └── 00_environment.ipynb
│
├── src/
│   └── check_environment.py
│
├── tests/
├── .gitignore
├── README.md
└── requirements.txt
```

---

## 8. Crear carpetas desde PowerShell

```powershell
mkdir data, docs, firmware, images, notebooks, src, tests
mkdir data\raw, data\processed
mkdir src\data_generation, src\data_processing, src\visualization
```

---

## 9. Archivo `.gitignore`

Creamos un archivo llamado `.gitignore` en la raíz del proyecto.

Contenido recomendado:

```text
# Virtual environments
.venv/

# Python cache
__pycache__/
*.py[cod]

# Jupyter
.ipynb_checkpoints/

# Environment variables
.env

# OS files
.DS_Store
Thumbs.db

# Logs and temporary files
*.log
*.tmp
```

Objetivo: evitar subir a GitHub archivos innecesarios como `.venv`.

---

## 10. Archivo de prueba del entorno

Creamos el archivo:

```text
src/check_environment.py
```

Contenido:

```python
"""Check that the initial data analysis environment is working."""

import matplotlib
import numpy as np
import pandas as pd


def main() -> None:
    """Print installed package versions and run a small calculation."""
    temperatures = np.array([18.5, 19.2, 20.1, 21.0, 20.4])

    dataframe = pd.DataFrame(
        {
            "temperature_c": temperatures,
        }
    )

    print("Environment is working.")
    print(f"NumPy version: {np.__version__}")
    print(f"pandas version: {pd.__version__}")
    print(f"matplotlib version: {matplotlib.__version__}")
    print(f"Average temperature: {dataframe['temperature_c'].mean():.2f} °C")


if __name__ == "__main__":
    main()
```

Ejecutar desde la raíz del proyecto:

```powershell
py src\check_environment.py
```

Salida esperada:

```text
Environment is working.
NumPy version: ...
pandas version: ...
matplotlib version: ...
Average temperature: 19.84 °C
```

---

## 11. Configuración básica de VS Code

La carpeta `.vscode` debe ir en la raíz del proyecto, no dentro de `src`.

Estructura correcta:

```text
smart-weather-station-ai-lab/
├── .vscode/
│   └── settings.json
├── src/
│   └── check_environment.py
```

Contenido de `.vscode/settings.json`:

```json
{
  "python.defaultInterpreterPath": ".venv\\Scripts\\python.exe",
  "python.terminal.activateEnvironment": true,
  "editor.formatOnSave": true,
  "files.exclude": {
    "**/__pycache__": true,
    "**/.ipynb_checkpoints": true
  }
}
```

---

## 12. Seleccionar intérprete en VS Code

En VS Code:

```text
Ctrl + Shift + P
Python: Select Interpreter
```

Seleccionar:

```text
.venv\Scripts\python.exe
```

O algo parecido a:

```text
Python 3.12.0 ('.venv': venv)
```

Esto asegura que VS Code use las librerías instaladas en el entorno virtual del proyecto.

---

## 13. Debugger en VS Code

Creamos o configuramos:

```text
.vscode/launch.json
```

Contenido recomendado:

```json
{
  "version": "0.2.0",
  "configurations": [
    {
      "name": "Python: Run current file",
      "type": "debugpy",
      "request": "launch",
      "program": "${file}",
      "console": "integratedTerminal",
      "justMyCode": true
    },
    {
      "name": "Python: Check environment",
      "type": "debugpy",
      "request": "launch",
      "program": "${workspaceFolder}/src/check_environment.py",
      "console": "integratedTerminal",
      "justMyCode": true
    }
  ]
}
```

Uso:

1. Abrir `src/check_environment.py`.
2. Poner un breakpoint.
3. Ir a `Run and Debug`.
4. Seleccionar `Python: Check environment`.
5. Pulsar Play.
6. Revisar variables en el panel izquierdo.

---

## 14. JupyterLab

Ejecutar JupyterLab:

```powershell
jupyter lab
```

Si se abre el Bloc de notas en vez del navegador, usar:

```powershell
jupyter lab --no-browser
```

Luego copiar en Chrome o Edge la URL que empieza por:

```text
http://localhost:8888/lab?token=
```

No copiar la ruta que empieza por:

```text
file:///C:/Users/...
```

La URL buena es la de `localhost`.

---

## 15. Notebook inicial

Creamos el notebook:

```text
notebooks/00_environment.ipynb
```

Objetivo:

* Comprobar que Jupyter funciona.
* Importar NumPy, pandas y matplotlib.
* Crear una tabla simple.
* Crear una gráfica simple.

Código de prueba:

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

temperatures = np.array([18.5, 19.2, 20.1, 21.0, 20.4])

df = pd.DataFrame({
    "sample": range(1, len(temperatures) + 1),
    "temperature_c": temperatures
})

df
```

Gráfica:

```python
plt.plot(df["sample"], df["temperature_c"], marker="o")
plt.title("Environment Test — Temperature Samples")
plt.xlabel("Sample")
plt.ylabel("Temperature (°C)")
plt.grid(True)
plt.show()
```

---

## 16. Inicializar Git

Git debe ejecutarse desde la raíz del proyecto:

```powershell
cd $HOME\Documents\AI-Master-2026-2028\smart-weather-station-ai-lab
```

Inicializar repositorio:

```powershell
git init
git status
```

Añadir archivos:

```powershell
git add .
```

Crear primer commit:

```powershell
git commit -m "Initialize Smart Weather Station AI Lab Project"
```

---

## 17. Corregir email de Git si usa correo corporativo

El primer commit usó automáticamente el correo corporativo.

Para configurar un email personal solo en este repositorio:

```powershell
git config user.name "Marcos Albetman"
git config user.email "TU_EMAIL_PERSONAL"
```

Corregir el autor del commit anterior:

```powershell
git commit --amend --reset-author
```

Comprobar último commit:

```powershell
git log --pretty=fuller -1
```

Comprobar estado:

```powershell
git status
```

Resultado ideal:

```text
nothing to commit, working tree clean
```

---

## 18. Comandos más usados

### Navegación

```powershell
pwd
cd ..
cd $HOME\Documents
cd $HOME\Documents\AI-Master-2026-2028\smart-weather-station-ai-lab
dir
```

### Python y entorno

```powershell
py --version
py -m venv .venv
.\.venv\Scripts\Activate.ps1
py -m pip install --upgrade pip
py -m pip install numpy pandas matplotlib jupyterlab ipykernel pytest ruff
py -m pip list
py -m pip freeze > requirements.txt
```

### Ejecutar scripts

```powershell
py src\check_environment.py
```

### Jupyter

```powershell
jupyter lab
jupyter lab --no-browser
```

### Git

```powershell
git init
git status
git add .
git commit -m "mensaje del commit"
git log --pretty=fuller -1
```

### VS Code

```powershell
code .
```

---

## 19. Errores que aparecieron y solución

### Error: Python no encontrado

Problema:

```text
Python was not found
```

Solución: usar `py` en lugar de `python`.

```powershell
py --version
```

---

### Error: no module named matplotlib

Problema:

```text
ModuleNotFoundError: No module named 'matplotlib'
```

Causa: librerías no instaladas en el entorno activo.

Solución:

```powershell
.\.venv\Scripts\Activate.ps1
py -m pip install numpy pandas matplotlib jupyterlab ipykernel pytest ruff
```

---

### Error: no se encuentra `.venv`

Causa: estabas en la carpeta incorrecta.

Solución: entrar a la carpeta del proyecto.

```powershell
cd $HOME\Documents\AI-Master-2026-2028\smart-weather-station-ai-lab
```

---

### Jupyter abre Bloc de notas

Causa: Windows tiene los archivos `.html` asociados al Bloc de notas.

Solución rápida:

```powershell
jupyter lab --no-browser
```

Luego copiar en navegador la URL que empieza por:

```text
http://localhost:8888/lab?token=
```

---

## 20. Próximo paso del proyecto

El siguiente paso será ir al chat:

```text
03 — Python para IA
```

Y crear el notebook:

```text
notebooks/01_synthetic_weather_data_analysis.ipynb
```

Objetivo del siguiente notebook:

1. Generar datos meteorológicos sintéticos.
2. Guardarlos en `data/raw/synthetic_weather_data.csv`.
3. Cargarlos con pandas.
4. Visualizar temperatura, humedad, presión y luz.
5. Calcular estadísticas básicas.
6. Escribir conclusiones sencillas.

Prompt recomendado para el Chat 03:

```text
Estamos en la Semana 1 del Mes 1 del roadmap IA 2026-2028.

Ya he creado el entorno Python del proyecto Smart Weather Station AI Lab.

Quiero crear el primer notebook:
notebooks/01_synthetic_weather_data_analysis.ipynb

Ayúdame paso a paso a:
1. Generar datos meteorológicos sintéticos.
2. Guardarlos en data/raw/synthetic_weather_data.csv.
3. Cargarlos con pandas.
4. Visualizar temperatura, humedad, presión y luz.
5. Calcular estadísticas básicas.
6. Escribir conclusiones sencillas.
```

---

## 21. Concepto aprendido

Lo importante de esta sesión no fue solo instalar herramientas.

Aprendimos un flujo profesional básico:

```text
Proyecto → entorno virtual → dependencias → script de prueba → VS Code → debugger → notebook → Git → commit
```

Este flujo será la base de todos los proyectos futuros de IA.

