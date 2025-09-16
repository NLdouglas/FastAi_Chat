from http import HTTPStatus

from fastapi import FastAPI

from fast_chat.schemas import Message, UserSchema, PuplicUser

chatV1 = FastAPI()


@chatV1.get('/', status_code=HTTPStatus.OK, response_model=Message)
def read_root():
    return {'message': 'Welcome to FastChat!'}


@chatV1.post('/Users/', status_code=HTTPStatus.CREATED, response_model= PuplicUser)
def create_user(user: UserSchema):
    return user
