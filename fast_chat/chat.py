from fastapi import FastAPI

chatV1 = FastAPI()


@chatV1.get('/')
def read_root():
    return {'message': 'Welcome to FastChat!'}
