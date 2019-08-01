import struct

FNV_OFFSET_BASIS_64 = 14695981039346656037
FNV_PRIME_64        = 1099511628211
FNV_BITMASK_64      = 18446744073709551615

def hash_exec(str):
    hash = FNV_OFFSET_BASIS_64
    for b in str.encode():
        hash = (FNV_PRIME_64 * hash) ^ b
        hash = hash & FNV_BITMASK_64
    return hash
