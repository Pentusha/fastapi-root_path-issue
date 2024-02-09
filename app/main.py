from operator import itemgetter

from fastapi import FastAPI, APIRouter, Request

auth_router = APIRouter()
users_router = APIRouter()


def get_resp(request: Request):
    return {
        'path': request.scope['path'],
        'raw_path': request.scope['raw_path'].decode(),
        'root_path': request.scope['root_path'],
    }


@auth_router.get('/')
async def return_paths_auth(request: Request):
    return get_resp(request)


@users_router.get('/')
async def return_paths_users(request: Request):
    return get_resp(request)


router = APIRouter()
router.include_router(auth_router, prefix='/auth')
router.include_router(users_router, prefix='/users')
app = FastAPI(root_path='/auth')
app.include_router(router)
