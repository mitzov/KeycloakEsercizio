from jose import jwt

KEYCLOAK_PUBLIC_KEY = "CHIAVE_PUBBLICA_KEYCLOAK"

def decode_token(token):

    decoded = jwt.decode(
        token,
        KEYCLOAK_PUBLIC_KEY,
        algorithms=["RS256"],
        audience="account"
    )

    return decoded