import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s')

project_name = "hate_classification"

list_of_files = [
    f"{project_name}/components/__init__.py",
    f"{project_name}/components/data_ingestion.py",
    f"{project_name}/components/data_transformation.py",
    f"{project_name}/components/model_evaluation.py",
    f"{project_name}/components/model_trainer.py",
    f"{project_name}/components/model_pusher.py",
    f"{project_name}/configuration/__init__.py",
    f"{project_name}/configuration/gcloud_syncer.py",
    f"{project_name}/constant/__init__.py",
    f"{project_name}/entity/__init__.py",
    f"{project_name}/entity/artifact_entity.py",
    f"{project_name}/entity/config_entity.py",
    f"{project_name}/exception/__init__.py",
    f"{project_name}/logger/__init__.py",
    f"{project_name}/pipleline/__init__.py",
    f"{project_name}/pipleline/prediction_pipeline.py",
    f"{project_name}/pipleline/train_pipeline.py",
    f"{project_name}/ml/__init__.py",
    f"{project_name}/ml/feature.py",
    "app.py",
    "demo.py",
    "requirements.txt",
    "Dockerfile",
    ".dockerignore",
    "setup.py"
]


# for filepath in list_of_files:
#     filepath = Path(filepath)

#     filedir, filename = os.path.split(filepath)

#     if filedir !="":
#         os.makedirs(filedir, exist_ok=True)
#         logging.info(f"Creating directory; {filedir} for the file: {filename}")

#     if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
#         with open(filepath, 'w') as f:
#             logging.info(f"Creating empty files: {filepath}")

#     else:
#         logging.info(f"{filename} already exists")

for filepath in list_of_files:
    filepath = Path(filepath)  # Ensure filepath is a Path object
    filedir = filepath.parent  # Get the parent directory
    filename = filepath.name   # Get the file name

    # Ensure the directory exists
    if not filedir.exists():
        filedir.mkdir(parents=True, exist_ok=True)
        logging.info(f"Created directory: {filedir} for the file: {filename}")

    # Check if the file needs to be created or is empty
    if not filepath.exists() or filepath.stat().st_size == 0:
        filepath.touch()  # Create an empty file
        logging.info(f"Created empty file: {filepath}")
    else:
        logging.info(f"{filename} already exists")