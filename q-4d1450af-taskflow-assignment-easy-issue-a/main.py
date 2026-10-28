import jwt

# TaskFlow issues HS256 access tokens carrying who the user is ("sub")
# and what they can do ("role"). Implement the three helpers below.

def issue_token(user_id, role, secret):
    """Return an HS256 JWT whose payload is {"sub": user_id, "role": role}."""
    payload = {"sub": user_id, "role": role}
    return jwt.encode(payload, key=secret, algorithm="HS256")


def read_claims(token, secret):
    """Decode the token and return its claims dict."""
    return jwt.decode(token, key=secret, algorithms=["HS256"])

def token_is_valid(token, secret):
    """Return True if the token decodes under `secret`, else False."""
    try:
        read_claims(token, secret)
    except jwt.InvalidTokenError:
        return False
    return True

