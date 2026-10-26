import hashlib
import hmac

ITERATIONS = 100000

def hash_password(password, salt, iterations=ITERATIONS):
    """Return hashlib.pbkdf2_hmac('sha256', ...) as a hex string.
    salt is bytes; encode the password as utf-8."""
    return hashlib.pbkdf2_hmac(
        'sha256', password.encode('utf-8'), salt, iterations
    ).hex()

def make_record(password, salt, iterations=ITERATIONS):
    """Return a record string 'iterations$salt_hex$hash_hex'
    (use salt.hex() for the salt portion)."""
    return f'{iterations}${salt.hex()}${hash_password(password, salt, iterations)}'

def verify_password(password, record):
    """Parse record back into iterations/salt/hash, recompute the hash for
    `password`, and return True only if it matches. Return False for any
    malformed record instead of raising."""
    try:
        iterations_text, salt_hex, expected_hash = record.split('$')
        iterations = int(iterations_text)
        if iterations <= 0:
            return False
        salt = bytes.fromhex(salt_hex)
        actual_hash = hash_password(password, salt, iterations)
        return hmac.compare_digest(actual_hash, expected_hash)
    except (AttributeError, TypeError, ValueError, OverflowError):
        return False