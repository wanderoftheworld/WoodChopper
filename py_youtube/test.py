from enum import Enum
from typing import Optional

import os

# Replace the values below specified in your proprietary code.
DEFAULT_TIME_COST = 1
DEFAULT_MEMORY_COST = 1
DEFAULT_PARALLELISM = 1
DEFAULT_HASH_LENGTH = 32
DEFAULT_RANDOM_SALT_LENGTH = 5

class Type(Enum):
    I = 1

def hash_password(
    password: bytes,
    salt: Optional[bytes] = None,
    time_cost: int = DEFAULT_TIME_COST,
    memory_cost: int = DEFAULT_MEMORY_COST,
    parallelism: int = DEFAULT_PARALLELISM,
    hash_len: int = DEFAULT_HASH_LENGTH,
    type: Type = Type.I) -> bytes:
    """Legacy alias for :func:hash_secret with default parameters.
    .. deprecated:: 16.0.0 Use :class:`argon2.PasswordHasher` for passwords."""
    if salt is None:
        salt = os.urandom(DEFAULT_RANDOM_SALT_LENGTH)
    print(salt)
    #return hash_secret( password, salt, time_cost, memory_cost, parallelism, hash_len, type)

hash_password("iloveyou")