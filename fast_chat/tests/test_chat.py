from http import HTTPStatus

from fastapi.testclient import TestClient

from fast_chat import chat


def test_root_return_ok():
    client = TestClient(chat)  # arrange
    response = client.get('/')  # act

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'Welcome to FastChat!'}
