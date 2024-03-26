from fastapi import FastAPI, Depends, UploadFile
from fastapi.responses import FileResponse

from src.files import try_load, save, delete
from src.database import create_connection
from src.auth import get_email

import os.path


app = FastAPI()


def set_avatar_field(email: str, value: bool):
    with create_connection() as db, db.cursor(dictionary=True) as cursor:
        cursor.execute(f"""
        update users
        set has_avatar = {1 if value else 0}
        where email = '{email}'""")
        db.commit()


@app.get("/avatar")
def get_avatar(email: str) -> FileResponse:
    return try_load(email + ".jpg")


@app.post("/add_avatar")
def load_avatar(
    avatar: UploadFile,
    email = Depends(get_email)
):
    save(avatar, email + ".jpg")
    set_avatar_field(email, True)
    return "OK"


@app.post("/remove_avatar")
def remove_avatar(email: str = Depends(get_email)):
    delete(email + ".jpg")
    set_avatar_field(email, False)
    return "OK"