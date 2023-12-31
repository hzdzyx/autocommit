import json
import os

KEY_FILE = '../key.config'


def get_key_from_file():
    if os.path.exists(KEY_FILE):
        with open(KEY_FILE, 'r') as f:
            data = json.load(f)
            return data.get('key')

    return None


def save_key_to_file(key):
    with open(KEY_FILE, 'w') as f:
        json.dump({'key': key}, f)
