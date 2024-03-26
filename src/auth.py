from typing import Annotated

from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer, HTTPBearer, HTTPAuthorizationCredentials
from starlette import status
from jose import JWTError, jwt

import src.config as config

security = HTTPBearer()

def get_email(authorization: Annotated[HTTPAuthorizationCredentials, Depends(security)]) -> str:
    token = authorization.credentials
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, config.secret_key, algorithms=[config.algorithm])
        email: str = payload.get("sub")
        version: str = payload.get("ver")
        if email is None or version != config.version:
            raise credentials_exception
    except JWTError:
        raise credentials_exception
    return email