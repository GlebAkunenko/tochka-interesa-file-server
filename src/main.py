from fastapi import FastAPI, Depends, UploadFile
from fastapi.responses import FileResponse

from src.files import try_load, save, delete
from src.database import create_connection
from src.auth import get_email


app = FastAPI(
    title="Tochka Interesa File Server"
)


@app.get("/avatar")
def get_avatar(email: str) -> FileResponse:
    return try_load(email + ".jpg")


@app.post("/add_avatar")
def load_avatar(
    avatar: UploadFile,
    email = Depends(get_email)
):
    save(avatar, email + ".jpg")
    return "OK"


@app.post("/remove_avatar")
def remove_avatar(email: str = Depends(get_email)):
    delete(email + ".jpg")
    return "OK"