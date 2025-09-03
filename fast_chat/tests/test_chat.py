from fastapi.testclient import TestClient

from fast_chat.chat import chat

client = TestClient(chat)
