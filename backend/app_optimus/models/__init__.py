import os
import importlib

# Carrega automaticamente todos os módulos dentro do diretório
current_dir = os.path.dirname(__file__)
modules = [
    f[:-3]
    for f in os.listdir(current_dir)
    if f.endswith(".py") and f != "__init__.py"
]

for module in modules:
    importlib.import_module(f"app_optimus.models.{module}")
