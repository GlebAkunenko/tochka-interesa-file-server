from fastapi import UploadFile
from fastapi.responses import FileResponse
import os.path
from src.config import data_path as dir_path


def save(file: UploadFile, filename: str | None = None) -> str:
    name = filename if filename is not None else file.filename
    path = fr"{dir_path}/{name}"
    with open(path, "wb") as buffer:
        buffer.write(file.file.read())
    return name


def try_load(filename: str) -> FileResponse | None:
    if not os.path.isfile(rf"{dir_path}/{filename}"):
        return None
    return FileResponse(rf"{dir_path}/{filename}")


def delete(filename: str):
    path = rf"{dir_path}/{filename}"
    if os.path.exists(path):
        os.remove(path)