import jwt

# TaskFlow now issues tokens that may carry an expiry ("exp") and must be
# verified with clear, distinct outcomes for the caller.

def issue_token(user_id, role, secret, exp_ts=None):
    """Sign {"sub": user_id, "role": role} (add "exp": exp_ts when given)."""
    payload = {"sub": user_id, "role": role}
    if exp_ts is not None:
        payload["exp"] = exp_ts
    return jwt.encode(payload, key=secret, algorithm="HS256")

def verify_token(token, secret):
    """Return the claims dict when valid; otherwise return one of the strings
    "expired", "invalid_signature", or "invalid_token"."""
    try:
        return jwt.decode(token, key=secret, algorithms=["HS256"])
    except jwt.ExpiredSignatureError:
        return "expired"
    except jwt.InvalidSignatureError:
        return "invalid_signature"
    except jwt.InvalidTokenError:
        return "invalid_token"

def extract_role(token, secret):
    """Return the role string, or "invalid" if the token cannot be trusted."""
    claims = verify_token(token, secret)
    if not isinstance(claims, dict):
        return "invalid"
    role = claims.get("role")
    return role if isinstance(role, str) else "invalid"