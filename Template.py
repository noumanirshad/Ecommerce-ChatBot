import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

project_name =  'Project_Name'

list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/components/data_ingestion.py",
    f"src/components/data_transformation.py",
    f"src/components/model_trainer.py",
    f"src/components/model_evaluation.py",
    f"src/pipeline/__init__.py",
    f"src/pipeline/training_pipeline.py",
    f"src/pipeline/prediction_pipeline.py",
    f"src/utils/__init__.py",
    f"src/utils/utils.py",
    f"src/logger/logging.py",
    f"src/logger/exception.py",
    f"tests/unit/__init__.py",
    f"tests/integration/__init__.py",
    f"experiment/experiments.ipynb"
    "init_setup.sh",
    "requirements.txt",
    "requirements_dev.txt",
    "setup.py",
    "setup.cfg",
    "pyproject.toml",
    "tox.ini",
    "app.py",   
    "main.py",   
    "Dockerfile",
]

for file_path in list_of_files:
    file_path = Path(file_path)
    filedir, filename = os.path.split(file_path)

    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Created directory: {filedir} for the file {filename}")

    if (not os.path.exists(file_path)) or (os.path.getsize(file_path)== 0):
        with open(file_path, "w") as f:
            pass
            logging.info(f"Created empty file: {file_path}")

    else:
        logging.info(f"{filename} is already exists")