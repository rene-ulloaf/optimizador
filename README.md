# Django Optimización de Producción

Este proyecto es una aplicación web desarrollada en Django que resuelve un problema de optimización lineal y genera un gráfico interactivo con Matplotlib para visualizar la región factible y la solución óptima.

---

## Requisitos

- Python 3.10 o superior
- pip (gestor de paquetes)
- Virtualenv (opcional pero recomendado)

---

## 🧱 Instalación
**Clona el repositorio:**

```bash
git clone https://github.com/rene-ulloaf/optimizador.git
cd tu_repositorio

#Opcional
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows

Configuración del entorno
pip install -r requirements.txt


Ejecución del servidor
python manage.py runserver
Abre tu navegador en: http://localhost:8000/

Testing

#Crea el archivo pytest.ini si no existe para usar pytest si vas a hacer testing:
[pytest]
DJANGO_SETTINGS_MODULE = tu_proyecto.settings
python_files = tests.py test_*.py *_tests.py

pytest
