
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


from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.app.routes import auth, mood, stats
from backend.app import models, database
from fastapi.security import OAuth2PasswordBearer
from fastapi.openapi.utils import get_openapi

app = FastAPI(title="Mood Diary API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router, prefix="/auth")
app.include_router(mood.router, prefix="/mood")
app.include_router(stats.router, prefix="/stats")


@app.get("/")
def read_root():
    return {"msg": "Welcome to Mood Diary API"}


# Create tables
models.Base.metadata.create_all(bind=database.engine)


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")


def x_custom_openapi__mutmut_orig():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="Mood Diary API",
        version="1.0.0",
        description="Track your mood history with secure login.",
        routes=app.routes,
    )
    openapi_schema["components"]["securitySchemes"] = {
        "OAuth2PasswordBearer": {
            "type": "http",
            "scheme": "bearer",
            "bearerFormat": "JWT"
        }
    }
    for path in openapi_schema["paths"].values():
        for method in path.values():
            method["security"] = [{"OAuth2PasswordBearer": []}]
    app.openapi_schema = openapi_schema
    return app.openapi_schema


def x_custom_openapi__mutmut_1():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="XXMood Diary APIXX",
        version="1.0.0",
        description="Track your mood history with secure login.",
        routes=app.routes,
    )
    openapi_schema["components"]["securitySchemes"] = {
        "OAuth2PasswordBearer": {
            "type": "http",
            "scheme": "bearer",
            "bearerFormat": "JWT"
        }
    }
    for path in openapi_schema["paths"].values():
        for method in path.values():
            method["security"] = [{"OAuth2PasswordBearer": []}]
    app.openapi_schema = openapi_schema
    return app.openapi_schema


def x_custom_openapi__mutmut_2():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="Mood Diary API",
        version="XX1.0.0XX",
        description="Track your mood history with secure login.",
        routes=app.routes,
    )
    openapi_schema["components"]["securitySchemes"] = {
        "OAuth2PasswordBearer": {
            "type": "http",
            "scheme": "bearer",
            "bearerFormat": "JWT"
        }
    }
    for path in openapi_schema["paths"].values():
        for method in path.values():
            method["security"] = [{"OAuth2PasswordBearer": []}]
    app.openapi_schema = openapi_schema
    return app.openapi_schema


def x_custom_openapi__mutmut_3():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="Mood Diary API",
        version="1.0.0",
        description="XXTrack your mood history with secure login.XX",
        routes=app.routes,
    )
    openapi_schema["components"]["securitySchemes"] = {
        "OAuth2PasswordBearer": {
            "type": "http",
            "scheme": "bearer",
            "bearerFormat": "JWT"
        }
    }
    for path in openapi_schema["paths"].values():
        for method in path.values():
            method["security"] = [{"OAuth2PasswordBearer": []}]
    app.openapi_schema = openapi_schema
    return app.openapi_schema


def x_custom_openapi__mutmut_4():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        version="1.0.0",
        description="Track your mood history with secure login.",
        routes=app.routes,
    )
    openapi_schema["components"]["securitySchemes"] = {
        "OAuth2PasswordBearer": {
            "type": "http",
            "scheme": "bearer",
            "bearerFormat": "JWT"
        }
    }
    for path in openapi_schema["paths"].values():
        for method in path.values():
            method["security"] = [{"OAuth2PasswordBearer": []}]
    app.openapi_schema = openapi_schema
    return app.openapi_schema


def x_custom_openapi__mutmut_5():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="Mood Diary API",
        description="Track your mood history with secure login.",
        routes=app.routes,
    )
    openapi_schema["components"]["securitySchemes"] = {
        "OAuth2PasswordBearer": {
            "type": "http",
            "scheme": "bearer",
            "bearerFormat": "JWT"
        }
    }
    for path in openapi_schema["paths"].values():
        for method in path.values():
            method["security"] = [{"OAuth2PasswordBearer": []}]
    app.openapi_schema = openapi_schema
    return app.openapi_schema


def x_custom_openapi__mutmut_6():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="Mood Diary API",
        version="1.0.0",
        routes=app.routes,
    )
    openapi_schema["components"]["securitySchemes"] = {
        "OAuth2PasswordBearer": {
            "type": "http",
            "scheme": "bearer",
            "bearerFormat": "JWT"
        }
    }
    for path in openapi_schema["paths"].values():
        for method in path.values():
            method["security"] = [{"OAuth2PasswordBearer": []}]
    app.openapi_schema = openapi_schema
    return app.openapi_schema


def x_custom_openapi__mutmut_7():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="Mood Diary API",
        version="1.0.0",
        description="Track your mood history with secure login.",
    )
    openapi_schema["components"]["securitySchemes"] = {
        "OAuth2PasswordBearer": {
            "type": "http",
            "scheme": "bearer",
            "bearerFormat": "JWT"
        }
    }
    for path in openapi_schema["paths"].values():
        for method in path.values():
            method["security"] = [{"OAuth2PasswordBearer": []}]
    app.openapi_schema = openapi_schema
    return app.openapi_schema


def x_custom_openapi__mutmut_8():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = None
    openapi_schema["components"]["securitySchemes"] = {
        "OAuth2PasswordBearer": {
            "type": "http",
            "scheme": "bearer",
            "bearerFormat": "JWT"
        }
    }
    for path in openapi_schema["paths"].values():
        for method in path.values():
            method["security"] = [{"OAuth2PasswordBearer": []}]
    app.openapi_schema = openapi_schema
    return app.openapi_schema


def x_custom_openapi__mutmut_9():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="Mood Diary API",
        version="1.0.0",
        description="Track your mood history with secure login.",
        routes=app.routes,
    )
    openapi_schema["XXcomponentsXX"]["securitySchemes"] = {
        "OAuth2PasswordBearer": {
            "type": "http",
            "scheme": "bearer",
            "bearerFormat": "JWT"
        }
    }
    for path in openapi_schema["paths"].values():
        for method in path.values():
            method["security"] = [{"OAuth2PasswordBearer": []}]
    app.openapi_schema = openapi_schema
    return app.openapi_schema


def x_custom_openapi__mutmut_10():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="Mood Diary API",
        version="1.0.0",
        description="Track your mood history with secure login.",
        routes=app.routes,
    )
    openapi_schema[None]["securitySchemes"] = {
        "OAuth2PasswordBearer": {
            "type": "http",
            "scheme": "bearer",
            "bearerFormat": "JWT"
        }
    }
    for path in openapi_schema["paths"].values():
        for method in path.values():
            method["security"] = [{"OAuth2PasswordBearer": []}]
    app.openapi_schema = openapi_schema
    return app.openapi_schema


def x_custom_openapi__mutmut_11():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="Mood Diary API",
        version="1.0.0",
        description="Track your mood history with secure login.",
        routes=app.routes,
    )
    openapi_schema["components"]["XXsecuritySchemesXX"] = {
        "OAuth2PasswordBearer": {
            "type": "http",
            "scheme": "bearer",
            "bearerFormat": "JWT"
        }
    }
    for path in openapi_schema["paths"].values():
        for method in path.values():
            method["security"] = [{"OAuth2PasswordBearer": []}]
    app.openapi_schema = openapi_schema
    return app.openapi_schema


def x_custom_openapi__mutmut_12():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="Mood Diary API",
        version="1.0.0",
        description="Track your mood history with secure login.",
        routes=app.routes,
    )
    openapi_schema["components"][None] = {
        "OAuth2PasswordBearer": {
            "type": "http",
            "scheme": "bearer",
            "bearerFormat": "JWT"
        }
    }
    for path in openapi_schema["paths"].values():
        for method in path.values():
            method["security"] = [{"OAuth2PasswordBearer": []}]
    app.openapi_schema = openapi_schema
    return app.openapi_schema


def x_custom_openapi__mutmut_13():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="Mood Diary API",
        version="1.0.0",
        description="Track your mood history with secure login.",
        routes=app.routes,
    )
    openapi_schema["components"]["securitySchemes"] = {
        "XXOAuth2PasswordBearerXX": {
            "type": "http",
            "scheme": "bearer",
            "bearerFormat": "JWT"
        }
    }
    for path in openapi_schema["paths"].values():
        for method in path.values():
            method["security"] = [{"OAuth2PasswordBearer": []}]
    app.openapi_schema = openapi_schema
    return app.openapi_schema


def x_custom_openapi__mutmut_14():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="Mood Diary API",
        version="1.0.0",
        description="Track your mood history with secure login.",
        routes=app.routes,
    )
    openapi_schema["components"]["securitySchemes"] = {
        "OAuth2PasswordBearer": {
            "XXtypeXX": "http",
            "scheme": "bearer",
            "bearerFormat": "JWT"
        }
    }
    for path in openapi_schema["paths"].values():
        for method in path.values():
            method["security"] = [{"OAuth2PasswordBearer": []}]
    app.openapi_schema = openapi_schema
    return app.openapi_schema


def x_custom_openapi__mutmut_15():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="Mood Diary API",
        version="1.0.0",
        description="Track your mood history with secure login.",
        routes=app.routes,
    )
    openapi_schema["components"]["securitySchemes"] = {
        "OAuth2PasswordBearer": {
            "type": "XXhttpXX",
            "scheme": "bearer",
            "bearerFormat": "JWT"
        }
    }
    for path in openapi_schema["paths"].values():
        for method in path.values():
            method["security"] = [{"OAuth2PasswordBearer": []}]
    app.openapi_schema = openapi_schema
    return app.openapi_schema


def x_custom_openapi__mutmut_16():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="Mood Diary API",
        version="1.0.0",
        description="Track your mood history with secure login.",
        routes=app.routes,
    )
    openapi_schema["components"]["securitySchemes"] = {
        "OAuth2PasswordBearer": {
            "type": "http",
            "XXschemeXX": "bearer",
            "bearerFormat": "JWT"
        }
    }
    for path in openapi_schema["paths"].values():
        for method in path.values():
            method["security"] = [{"OAuth2PasswordBearer": []}]
    app.openapi_schema = openapi_schema
    return app.openapi_schema


def x_custom_openapi__mutmut_17():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="Mood Diary API",
        version="1.0.0",
        description="Track your mood history with secure login.",
        routes=app.routes,
    )
    openapi_schema["components"]["securitySchemes"] = {
        "OAuth2PasswordBearer": {
            "type": "http",
            "scheme": "XXbearerXX",
            "bearerFormat": "JWT"
        }
    }
    for path in openapi_schema["paths"].values():
        for method in path.values():
            method["security"] = [{"OAuth2PasswordBearer": []}]
    app.openapi_schema = openapi_schema
    return app.openapi_schema


def x_custom_openapi__mutmut_18():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="Mood Diary API",
        version="1.0.0",
        description="Track your mood history with secure login.",
        routes=app.routes,
    )
    openapi_schema["components"]["securitySchemes"] = {
        "OAuth2PasswordBearer": {
            "type": "http",
            "scheme": "bearer",
            "XXbearerFormatXX": "JWT"
        }
    }
    for path in openapi_schema["paths"].values():
        for method in path.values():
            method["security"] = [{"OAuth2PasswordBearer": []}]
    app.openapi_schema = openapi_schema
    return app.openapi_schema


def x_custom_openapi__mutmut_19():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="Mood Diary API",
        version="1.0.0",
        description="Track your mood history with secure login.",
        routes=app.routes,
    )
    openapi_schema["components"]["securitySchemes"] = {
        "OAuth2PasswordBearer": {
            "type": "http",
            "scheme": "bearer",
            "bearerFormat": "XXJWTXX"
        }
    }
    for path in openapi_schema["paths"].values():
        for method in path.values():
            method["security"] = [{"OAuth2PasswordBearer": []}]
    app.openapi_schema = openapi_schema
    return app.openapi_schema


def x_custom_openapi__mutmut_20():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="Mood Diary API",
        version="1.0.0",
        description="Track your mood history with secure login.",
        routes=app.routes,
    )
    openapi_schema["components"]["securitySchemes"] = None
    for path in openapi_schema["paths"].values():
        for method in path.values():
            method["security"] = [{"OAuth2PasswordBearer": []}]
    app.openapi_schema = openapi_schema
    return app.openapi_schema


def x_custom_openapi__mutmut_21():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="Mood Diary API",
        version="1.0.0",
        description="Track your mood history with secure login.",
        routes=app.routes,
    )
    openapi_schema["components"]["securitySchemes"] = {
        "OAuth2PasswordBearer": {
            "type": "http",
            "scheme": "bearer",
            "bearerFormat": "JWT"
        }
    }
    for path in openapi_schema["XXpathsXX"].values():
        for method in path.values():
            method["security"] = [{"OAuth2PasswordBearer": []}]
    app.openapi_schema = openapi_schema
    return app.openapi_schema


def x_custom_openapi__mutmut_22():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="Mood Diary API",
        version="1.0.0",
        description="Track your mood history with secure login.",
        routes=app.routes,
    )
    openapi_schema["components"]["securitySchemes"] = {
        "OAuth2PasswordBearer": {
            "type": "http",
            "scheme": "bearer",
            "bearerFormat": "JWT"
        }
    }
    for path in openapi_schema[None].values():
        for method in path.values():
            method["security"] = [{"OAuth2PasswordBearer": []}]
    app.openapi_schema = openapi_schema
    return app.openapi_schema


def x_custom_openapi__mutmut_23():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="Mood Diary API",
        version="1.0.0",
        description="Track your mood history with secure login.",
        routes=app.routes,
    )
    openapi_schema["components"]["securitySchemes"] = {
        "OAuth2PasswordBearer": {
            "type": "http",
            "scheme": "bearer",
            "bearerFormat": "JWT"
        }
    }
    for path in openapi_schema["paths"].values():
        for method in path.values():
            method["XXsecurityXX"] = [{"OAuth2PasswordBearer": []}]
    app.openapi_schema = openapi_schema
    return app.openapi_schema


def x_custom_openapi__mutmut_24():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="Mood Diary API",
        version="1.0.0",
        description="Track your mood history with secure login.",
        routes=app.routes,
    )
    openapi_schema["components"]["securitySchemes"] = {
        "OAuth2PasswordBearer": {
            "type": "http",
            "scheme": "bearer",
            "bearerFormat": "JWT"
        }
    }
    for path in openapi_schema["paths"].values():
        for method in path.values():
            method[None] = [{"OAuth2PasswordBearer": []}]
    app.openapi_schema = openapi_schema
    return app.openapi_schema


def x_custom_openapi__mutmut_25():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="Mood Diary API",
        version="1.0.0",
        description="Track your mood history with secure login.",
        routes=app.routes,
    )
    openapi_schema["components"]["securitySchemes"] = {
        "OAuth2PasswordBearer": {
            "type": "http",
            "scheme": "bearer",
            "bearerFormat": "JWT"
        }
    }
    for path in openapi_schema["paths"].values():
        for method in path.values():
            method["security"] = [{"XXOAuth2PasswordBearerXX": []}]
    app.openapi_schema = openapi_schema
    return app.openapi_schema


def x_custom_openapi__mutmut_26():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="Mood Diary API",
        version="1.0.0",
        description="Track your mood history with secure login.",
        routes=app.routes,
    )
    openapi_schema["components"]["securitySchemes"] = {
        "OAuth2PasswordBearer": {
            "type": "http",
            "scheme": "bearer",
            "bearerFormat": "JWT"
        }
    }
    for path in openapi_schema["paths"].values():
        for method in path.values():
            method["security"] = None
    app.openapi_schema = openapi_schema
    return app.openapi_schema


def x_custom_openapi__mutmut_27():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="Mood Diary API",
        version="1.0.0",
        description="Track your mood history with secure login.",
        routes=app.routes,
    )
    openapi_schema["components"]["securitySchemes"] = {
        "OAuth2PasswordBearer": {
            "type": "http",
            "scheme": "bearer",
            "bearerFormat": "JWT"
        }
    }
    for path in openapi_schema["paths"].values():
        for method in path.values():
            method["security"] = [{"OAuth2PasswordBearer": []}]
    app.openapi_schema = None
    return app.openapi_schema

x_custom_openapi__mutmut_mutants = {
'x_custom_openapi__mutmut_1': x_custom_openapi__mutmut_1, 
    'x_custom_openapi__mutmut_2': x_custom_openapi__mutmut_2, 
    'x_custom_openapi__mutmut_3': x_custom_openapi__mutmut_3, 
    'x_custom_openapi__mutmut_4': x_custom_openapi__mutmut_4, 
    'x_custom_openapi__mutmut_5': x_custom_openapi__mutmut_5, 
    'x_custom_openapi__mutmut_6': x_custom_openapi__mutmut_6, 
    'x_custom_openapi__mutmut_7': x_custom_openapi__mutmut_7, 
    'x_custom_openapi__mutmut_8': x_custom_openapi__mutmut_8, 
    'x_custom_openapi__mutmut_9': x_custom_openapi__mutmut_9, 
    'x_custom_openapi__mutmut_10': x_custom_openapi__mutmut_10, 
    'x_custom_openapi__mutmut_11': x_custom_openapi__mutmut_11, 
    'x_custom_openapi__mutmut_12': x_custom_openapi__mutmut_12, 
    'x_custom_openapi__mutmut_13': x_custom_openapi__mutmut_13, 
    'x_custom_openapi__mutmut_14': x_custom_openapi__mutmut_14, 
    'x_custom_openapi__mutmut_15': x_custom_openapi__mutmut_15, 
    'x_custom_openapi__mutmut_16': x_custom_openapi__mutmut_16, 
    'x_custom_openapi__mutmut_17': x_custom_openapi__mutmut_17, 
    'x_custom_openapi__mutmut_18': x_custom_openapi__mutmut_18, 
    'x_custom_openapi__mutmut_19': x_custom_openapi__mutmut_19, 
    'x_custom_openapi__mutmut_20': x_custom_openapi__mutmut_20, 
    'x_custom_openapi__mutmut_21': x_custom_openapi__mutmut_21, 
    'x_custom_openapi__mutmut_22': x_custom_openapi__mutmut_22, 
    'x_custom_openapi__mutmut_23': x_custom_openapi__mutmut_23, 
    'x_custom_openapi__mutmut_24': x_custom_openapi__mutmut_24, 
    'x_custom_openapi__mutmut_25': x_custom_openapi__mutmut_25, 
    'x_custom_openapi__mutmut_26': x_custom_openapi__mutmut_26, 
    'x_custom_openapi__mutmut_27': x_custom_openapi__mutmut_27
}

def custom_openapi(*args, **kwargs):
    result = _mutmut_trampoline(x_custom_openapi__mutmut_orig, x_custom_openapi__mutmut_mutants, *args, **kwargs)
    return result 

custom_openapi.__signature__ = _mutmut_signature(x_custom_openapi__mutmut_orig)
x_custom_openapi__mutmut_orig.__name__ = 'x_custom_openapi'




app.openapi = custom_openapi
