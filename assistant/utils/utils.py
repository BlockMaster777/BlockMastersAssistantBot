# coding=utf8
import requests
import os
import base64


def check_dash_health(url: str = "https://dashblocks.org/health") -> bool:
    try:
        response = requests.get(url)
        return response.status_code == 200
    except requests.RequestException:
        return False


def generate_secret_key(length: int = 64) -> str:
    return os.urandom(length).hex()


def encode_b64(data: str) -> str:
    return base64.b64encode(data.encode()).decode()

def decode_b64(data: str) -> str:
    return base64.b64decode(data.encode()).decode()
