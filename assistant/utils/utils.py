import base64
import os

import requests


def check_dash_health(front_url: str = "https://dashblocks.org",
                      back_url: str = "https://api.dashblocks.org/users/15") \
        -> tuple[bool, str]:
    try:
        response1 = requests.get(back_url)
        response2 = requests.get(front_url)
        status = response1.status_code == 200 and response2.status_code == 200
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
