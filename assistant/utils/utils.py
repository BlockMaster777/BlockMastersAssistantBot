# coding=utf8
import requests
import os
import base64


def check_dash_health(url: str = "https://dashblocks.org/health") \
        -> tuple[bool, str]:
    status = False
    try:
        response = requests.get(url)
        status = response.status_code == 200
    except requests.RequestException:
        status = False
    if status:
        message = "✅ DashBlocks services are operational."
    else:
        message = "❗DashBlocks services are down."
    return status, message


def generate_secret_key(length: int = 64) -> str:
    return os.urandom(length).hex()


def encode_b64(data: str) -> str:
    return base64.b64encode(data.encode()).decode()

def decode_b64(data: str) -> str:
    return base64.b64decode(data.encode()).decode()
