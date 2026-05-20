import hashlib
import os

def hash_file(path, algo="sha256"):
    h = hashlib.new(algo)
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(8192), b""):
            h.update(chunk)
    return h.hexdigest()

def verify_checksum(path, expected):
    actual = hash_file(path)
    return actual == expected
