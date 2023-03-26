NAME = "my_package"
from . import math_operations, string_operations
import json


def load_config(filename):
    with open(filename) as f:
        config = json.load(f)
    return config

print("json.file:")

print(load_config('my_package\setup.json'))
