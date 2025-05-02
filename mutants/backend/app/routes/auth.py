
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


from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from passlib.context import CryptContext
from backend.app.auth_utils import create_access_token
from fastapi import Form


from backend.app import models, schemas, database

router = APIRouter()
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def x_hash_password__mutmut_orig(password: str) -> str:
    return pwd_context.hash(password)


def x_hash_password__mutmut_1(password: str) -> str:
    return pwd_context.hash(None)

x_hash_password__mutmut_mutants = {
'x_hash_password__mutmut_1': x_hash_password__mutmut_1
}

def hash_password(*args, **kwargs):
    result = _mutmut_trampoline(x_hash_password__mutmut_orig, x_hash_password__mutmut_mutants, *args, **kwargs)
    return result 

hash_password.__signature__ = _mutmut_signature(x_hash_password__mutmut_orig)
x_hash_password__mutmut_orig.__name__ = 'x_hash_password'




def x_verify_password__mutmut_orig(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)


def x_verify_password__mutmut_1(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(None, hashed_password)


def x_verify_password__mutmut_2(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, None)


def x_verify_password__mutmut_3(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify( hashed_password)


def x_verify_password__mutmut_4(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password,)

x_verify_password__mutmut_mutants = {
'x_verify_password__mutmut_1': x_verify_password__mutmut_1, 
    'x_verify_password__mutmut_2': x_verify_password__mutmut_2, 
    'x_verify_password__mutmut_3': x_verify_password__mutmut_3, 
    'x_verify_password__mutmut_4': x_verify_password__mutmut_4
}

def verify_password(*args, **kwargs):
    result = _mutmut_trampoline(x_verify_password__mutmut_orig, x_verify_password__mutmut_mutants, *args, **kwargs)
    return result 

verify_password.__signature__ = _mutmut_signature(x_verify_password__mutmut_orig)
x_verify_password__mutmut_orig.__name__ = 'x_verify_password'




@router.post("/register")
def register(user: schemas.UserCreate, db: Session = Depends(database.get_db)):
    db_user = db.query(models.User).filter(
        models.User.username == user.username).first()
    if db_user:
        raise HTTPException(status_code=400, detail="Username already taken")

    hashed_pw = hash_password(user.password)
    new_user = models.User(
        username=user.username, hashed_password=hashed_pw)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return {"msg": f"User '{user.username}' registered successfully."}


@router.post("/login")
def login(
    username: str = Form(...),
    password: str = Form(...),
    db: Session = Depends(database.get_db)
):
    db_user = db.query(models.User).filter(
        models.User.username == username).first()
    if not db_user or not verify_password(password, db_user.hashed_password):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    access_token = create_access_token(data={"sub": db_user.username})
    return {"access_token": access_token, "token_type": "bearer"}
