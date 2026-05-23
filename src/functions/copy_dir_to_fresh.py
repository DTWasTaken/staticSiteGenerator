import os
import shutil


def copy_dir_to_fresh(source: str, destination: str):
    if not os.path.exists(source):
        raise ValueError(f"Folder {source} not found")

    if os.path.exists(destination):
        shutil.rmtree(destination)

    shutil.copytree(source, destination)
