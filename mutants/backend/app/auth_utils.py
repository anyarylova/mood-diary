
from inspect import signature as _mutmut_signature

def _mutmut_trampoline(orig, mutants, *args, **kwargs):
    import os
    mutant_under_test = os.environ['MUTANT_UNDER_TEST']
    if mutant_under_test == 'fail':
        from mutmut.__main__ import MutmutProgrammaticFailException
        raise MutmutProgrammaticFailException('Failed programmatically')      
    elif mutant_under_test == 'stats':
        from mutmut.__main__ import record_trampoline_hit
        record_trampoline_hit(orig.__module__ + '.' + orig.__name__)
        result = orig(*args, **kwargs)
        return result  # for the yield case
    prefix = orig.__module__ + '.' + orig.__name__ + '__mutmut_'
    if not mutant_under_test.startswith(prefix):
        result = orig(*args, **kwargs)
        return result  # for the yield case
    mutant_name = mutant_under_test.rpartition('.')[-1]
    result = mutants[mutant_name](*args, **kwargs)
    return result


from inspect import signature as _mutmut_signature

def _mutmut_yield_from_trampoline(orig, mutants, *args, **kwargs):
    import os
    mutant_under_test = os.environ['MUTANT_UNDER_TEST']
    if mutant_under_test == 'fail':
        from mutmut.__main__ import MutmutProgrammaticFailException
        raise MutmutProgrammaticFailException('Failed programmatically')      
    elif mutant_under_test == 'stats':
        from mutmut.__main__ import record_trampoline_hit
        record_trampoline_hit(orig.__module__ + '.' + orig.__name__)
        result = yield from orig(*args, **kwargs)
        return result  # for the yield case
    prefix = orig.__module__ + '.' + orig.__name__ + '__mutmut_'
    if not mutant_under_test.startswith(prefix):
        result = yield from orig(*args, **kwargs)
        return result  # for the yield case
    mutant_name = mutant_under_test.rpartition('.')[-1]
    result = yield from mutants[mutant_name](*args, **kwargs)
    return result


from datetime import datetime, timedelta
from jose import JWTError, jwt
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from backend.app import models, database
import os
from dotenv import load_dotenv

load_dotenv()  # Loads variables from a .env file into environment

SECRET_KEY = os.getenv("SECRET_KEY", "TEST_SECRET_KEY")  # Default key for CI
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30


def x_create_access_token__mutmut_orig(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def x_create_access_token__mutmut_1(data: dict):
    to_encode = None
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def x_create_access_token__mutmut_2(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() - timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def x_create_access_token__mutmut_3(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=None)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def x_create_access_token__mutmut_4(data: dict):
    to_encode = data.copy()
    expire = None
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def x_create_access_token__mutmut_5(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"XXexpXX": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def x_create_access_token__mutmut_6(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(None, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def x_create_access_token__mutmut_7(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, None, algorithm=ALGORITHM)
    return encoded_jwt


def x_create_access_token__mutmut_8(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=None)
    return encoded_jwt


def x_create_access_token__mutmut_9(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode( SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def x_create_access_token__mutmut_10(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, algorithm=ALGORITHM)
    return encoded_jwt


def x_create_access_token__mutmut_11(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY,)
    return encoded_jwt


def x_create_access_token__mutmut_12(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = None
    return encoded_jwt

x_create_access_token__mutmut_mutants = {
'x_create_access_token__mutmut_1': x_create_access_token__mutmut_1, 
    'x_create_access_token__mutmut_2': x_create_access_token__mutmut_2, 
    'x_create_access_token__mutmut_3': x_create_access_token__mutmut_3, 
    'x_create_access_token__mutmut_4': x_create_access_token__mutmut_4, 
    'x_create_access_token__mutmut_5': x_create_access_token__mutmut_5, 
    'x_create_access_token__mutmut_6': x_create_access_token__mutmut_6, 
    'x_create_access_token__mutmut_7': x_create_access_token__mutmut_7, 
    'x_create_access_token__mutmut_8': x_create_access_token__mutmut_8, 
    'x_create_access_token__mutmut_9': x_create_access_token__mutmut_9, 
    'x_create_access_token__mutmut_10': x_create_access_token__mutmut_10, 
    'x_create_access_token__mutmut_11': x_create_access_token__mutmut_11, 
    'x_create_access_token__mutmut_12': x_create_access_token__mutmut_12
}

def create_access_token(*args, **kwargs):
    result = _mutmut_trampoline(x_create_access_token__mutmut_orig, x_create_access_token__mutmut_mutants, *args, **kwargs)
    return result 

create_access_token.__signature__ = _mutmut_signature(x_create_access_token__mutmut_orig)
x_create_access_token__mutmut_orig.__name__ = 'x_create_access_token'




def x_decode_access_token__mutmut_orig(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except JWTError:
        return None


def x_decode_access_token__mutmut_1(token: str):
    try:
        payload = jwt.decode(None, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except JWTError:
        return None


def x_decode_access_token__mutmut_2(token: str):
    try:
        payload = jwt.decode(token, None, algorithms=[ALGORITHM])
        return payload
    except JWTError:
        return None


def x_decode_access_token__mutmut_3(token: str):
    try:
        payload = jwt.decode( SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except JWTError:
        return None


def x_decode_access_token__mutmut_4(token: str):
    try:
        payload = jwt.decode(token, algorithms=[ALGORITHM])
        return payload
    except JWTError:
        return None


def x_decode_access_token__mutmut_5(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY,)
        return payload
    except JWTError:
        return None


def x_decode_access_token__mutmut_6(token: str):
    try:
        payload = None
        return payload
    except JWTError:
        return None

x_decode_access_token__mutmut_mutants = {
'x_decode_access_token__mutmut_1': x_decode_access_token__mutmut_1, 
    'x_decode_access_token__mutmut_2': x_decode_access_token__mutmut_2, 
    'x_decode_access_token__mutmut_3': x_decode_access_token__mutmut_3, 
    'x_decode_access_token__mutmut_4': x_decode_access_token__mutmut_4, 
    'x_decode_access_token__mutmut_5': x_decode_access_token__mutmut_5, 
    'x_decode_access_token__mutmut_6': x_decode_access_token__mutmut_6
}

def decode_access_token(*args, **kwargs):
    result = _mutmut_trampoline(x_decode_access_token__mutmut_orig, x_decode_access_token__mutmut_mutants, *args, **kwargs)
    return result 

decode_access_token.__signature__ = _mutmut_signature(x_decode_access_token__mutmut_orig)
x_decode_access_token__mutmut_orig.__name__ = 'x_decode_access_token'




oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/login")


def x_get_current_user__mutmut_orig(
    token: str = Depends(oauth2_scheme),
    db: Session = Depends(database.get_db)
):
    payload = decode_access_token(token)
    if payload is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token"
            )

    username: str = payload.get("sub")
    if username is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
              detail="Invalid token"
              )

    user = (
        db.query(models.User)
        .filter(models.User.username == username)
        .first()
        )
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
              detail="User not found"
              )

    return user


def x_get_current_user__mutmut_1(
    token: str = Depends(None),
    db: Session = Depends(database.get_db)
):
    payload = decode_access_token(token)
    if payload is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token"
            )

    username: str = payload.get("sub")
    if username is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
              detail="Invalid token"
              )

    user = (
        db.query(models.User)
        .filter(models.User.username == username)
        .first()
        )
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
              detail="User not found"
              )

    return user


def x_get_current_user__mutmut_2(
    token: str = Depends(oauth2_scheme),
    db: Session = Depends(database.get_db)
):
    payload = decode_access_token(None)
    if payload is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token"
            )

    username: str = payload.get("sub")
    if username is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
              detail="Invalid token"
              )

    user = (
        db.query(models.User)
        .filter(models.User.username == username)
        .first()
        )
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
              detail="User not found"
              )

    return user


def x_get_current_user__mutmut_3(
    token: str = Depends(oauth2_scheme),
    db: Session = Depends(database.get_db)
):
    payload = None
    if payload is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token"
            )

    username: str = payload.get("sub")
    if username is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
              detail="Invalid token"
              )

    user = (
        db.query(models.User)
        .filter(models.User.username == username)
        .first()
        )
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
              detail="User not found"
              )

    return user


def x_get_current_user__mutmut_4(
    token: str = Depends(oauth2_scheme),
    db: Session = Depends(database.get_db)
):
    payload = decode_access_token(token)
    if payload is not None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token"
            )

    username: str = payload.get("sub")
    if username is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
              detail="Invalid token"
              )

    user = (
        db.query(models.User)
        .filter(models.User.username == username)
        .first()
        )
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
              detail="User not found"
              )

    return user


def x_get_current_user__mutmut_5(
    token: str = Depends(oauth2_scheme),
    db: Session = Depends(database.get_db)
):
    payload = decode_access_token(token)
    if payload is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="XXInvalid tokenXX"
            )

    username: str = payload.get("sub")
    if username is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
              detail="Invalid token"
              )

    user = (
        db.query(models.User)
        .filter(models.User.username == username)
        .first()
        )
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
              detail="User not found"
              )

    return user


def x_get_current_user__mutmut_6(
    token: str = Depends(oauth2_scheme),
    db: Session = Depends(database.get_db)
):
    payload = decode_access_token(token)
    if payload is None:
        raise HTTPException(
            detail="Invalid token"
            )

    username: str = payload.get("sub")
    if username is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
              detail="Invalid token"
              )

    user = (
        db.query(models.User)
        .filter(models.User.username == username)
        .first()
        )
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
              detail="User not found"
              )

    return user


def x_get_current_user__mutmut_7(
    token: str = Depends(oauth2_scheme),
    db: Session = Depends(database.get_db)
):
    payload = decode_access_token(token)
    if payload is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            )

    username: str = payload.get("sub")
    if username is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
              detail="Invalid token"
              )

    user = (
        db.query(models.User)
        .filter(models.User.username == username)
        .first()
        )
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
              detail="User not found"
              )

    return user


def x_get_current_user__mutmut_8(
    token: str = Depends(oauth2_scheme),
    db: Session = Depends(database.get_db)
):
    payload = decode_access_token(token)
    if payload is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token"
            )

    username: str = None
    if username is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
              detail="Invalid token"
              )

    user = (
        db.query(models.User)
        .filter(models.User.username == username)
        .first()
        )
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
              detail="User not found"
              )

    return user


def x_get_current_user__mutmut_9(
    token: str = Depends(oauth2_scheme),
    db: Session = Depends(database.get_db)
):
    payload = decode_access_token(token)
    if payload is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token"
            )

    username: str = payload.get("sub")
    if username is not None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
              detail="Invalid token"
              )

    user = (
        db.query(models.User)
        .filter(models.User.username == username)
        .first()
        )
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
              detail="User not found"
              )

    return user


def x_get_current_user__mutmut_10(
    token: str = Depends(oauth2_scheme),
    db: Session = Depends(database.get_db)
):
    payload = decode_access_token(token)
    if payload is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token"
            )

    username: str = payload.get("sub")
    if username is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
              detail="XXInvalid tokenXX"
              )

    user = (
        db.query(models.User)
        .filter(models.User.username == username)
        .first()
        )
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
              detail="User not found"
              )

    return user


def x_get_current_user__mutmut_11(
    token: str = Depends(oauth2_scheme),
    db: Session = Depends(database.get_db)
):
    payload = decode_access_token(token)
    if payload is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token"
            )

    username: str = payload.get("sub")
    if username is None:
        raise HTTPException(
              detail="Invalid token"
              )

    user = (
        db.query(models.User)
        .filter(models.User.username == username)
        .first()
        )
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
              detail="User not found"
              )

    return user


def x_get_current_user__mutmut_12(
    token: str = Depends(oauth2_scheme),
    db: Session = Depends(database.get_db)
):
    payload = decode_access_token(token)
    if payload is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token"
            )

    username: str = payload.get("sub")
    if username is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
              )

    user = (
        db.query(models.User)
        .filter(models.User.username == username)
        .first()
        )
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
              detail="User not found"
              )

    return user


def x_get_current_user__mutmut_13(
    token: str = Depends(oauth2_scheme),
    db: Session = Depends(database.get_db)
):
    payload = decode_access_token(token)
    if payload is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token"
            )

    username: str = payload.get("sub")
    if username is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
              detail="Invalid token"
              )

    user = (
        db.query(models.User)
        .filter(models.User.username != username)
        .first()
        )
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
              detail="User not found"
              )

    return user


def x_get_current_user__mutmut_14(
    token: str = Depends(oauth2_scheme),
    db: Session = Depends(database.get_db)
):
    payload = decode_access_token(token)
    if payload is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token"
            )

    username: str = payload.get("sub")
    if username is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
              detail="Invalid token"
              )

    user = None
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
              detail="User not found"
              )

    return user


def x_get_current_user__mutmut_15(
    token: str = Depends(oauth2_scheme),
    db: Session = Depends(database.get_db)
):
    payload = decode_access_token(token)
    if payload is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token"
            )

    username: str = payload.get("sub")
    if username is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
              detail="Invalid token"
              )

    user = (
        db.query(models.User)
        .filter(models.User.username == username)
        .first()
        )
    if user is not None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
              detail="User not found"
              )

    return user


def x_get_current_user__mutmut_16(
    token: str = Depends(oauth2_scheme),
    db: Session = Depends(database.get_db)
):
    payload = decode_access_token(token)
    if payload is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token"
            )

    username: str = payload.get("sub")
    if username is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
              detail="Invalid token"
              )

    user = (
        db.query(models.User)
        .filter(models.User.username == username)
        .first()
        )
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
              detail="XXUser not foundXX"
              )

    return user


def x_get_current_user__mutmut_17(
    token: str = Depends(oauth2_scheme),
    db: Session = Depends(database.get_db)
):
    payload = decode_access_token(token)
    if payload is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token"
            )

    username: str = payload.get("sub")
    if username is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
              detail="Invalid token"
              )

    user = (
        db.query(models.User)
        .filter(models.User.username == username)
        .first()
        )
    if user is None:
        raise HTTPException(
              detail="User not found"
              )

    return user


def x_get_current_user__mutmut_18(
    token: str = Depends(oauth2_scheme),
    db: Session = Depends(database.get_db)
):
    payload = decode_access_token(token)
    if payload is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token"
            )

    username: str = payload.get("sub")
    if username is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
              detail="Invalid token"
              )

    user = (
        db.query(models.User)
        .filter(models.User.username == username)
        .first()
        )
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
              )

    return user

x_get_current_user__mutmut_mutants = {
'x_get_current_user__mutmut_1': x_get_current_user__mutmut_1, 
    'x_get_current_user__mutmut_2': x_get_current_user__mutmut_2, 
    'x_get_current_user__mutmut_3': x_get_current_user__mutmut_3, 
    'x_get_current_user__mutmut_4': x_get_current_user__mutmut_4, 
    'x_get_current_user__mutmut_5': x_get_current_user__mutmut_5, 
    'x_get_current_user__mutmut_6': x_get_current_user__mutmut_6, 
    'x_get_current_user__mutmut_7': x_get_current_user__mutmut_7, 
    'x_get_current_user__mutmut_8': x_get_current_user__mutmut_8, 
    'x_get_current_user__mutmut_9': x_get_current_user__mutmut_9, 
    'x_get_current_user__mutmut_10': x_get_current_user__mutmut_10, 
    'x_get_current_user__mutmut_11': x_get_current_user__mutmut_11, 
    'x_get_current_user__mutmut_12': x_get_current_user__mutmut_12, 
    'x_get_current_user__mutmut_13': x_get_current_user__mutmut_13, 
    'x_get_current_user__mutmut_14': x_get_current_user__mutmut_14, 
    'x_get_current_user__mutmut_15': x_get_current_user__mutmut_15, 
    'x_get_current_user__mutmut_16': x_get_current_user__mutmut_16, 
    'x_get_current_user__mutmut_17': x_get_current_user__mutmut_17, 
    'x_get_current_user__mutmut_18': x_get_current_user__mutmut_18
}

def get_current_user(*args, **kwargs):
    result = _mutmut_trampoline(x_get_current_user__mutmut_orig, x_get_current_user__mutmut_mutants, *args, **kwargs)
    return result 

get_current_user.__signature__ = _mutmut_signature(x_get_current_user__mutmut_orig)
x_get_current_user__mutmut_orig.__name__ = 'x_get_current_user'


