import os
import importlib

current_dir = os.path.dirname(__file__)
modules = [
    f[:-3]
    for f in os.listdir(current_dir)
    if f.endswith(".py") and f != "__init__.py"
]

for module in modules:
    try:
        importlib.import_module(f"app_optimus.views.{module}")
        print(f"Successfully imported: app_optimus.views.{module}")
    except Exception as e:
        print(f"Error importing module {module}: {e}")

try:
    from .ouvidoria import OuvidoriaViewSet
except ImportError as e:
    print(f"Could not import OuvidoriaViewSet: {e}")

__all__ = ["OuvidoriaViewSet"]
