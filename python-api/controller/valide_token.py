from flask import session
import jwt

def has_valid_token():
    token = session.get('token')

    if token:
        secret_key = 'fondes2023'

        try:
            payload = jwt.decode(token, secret_key, algorithms=['HS256'])
            # Vérification du payload
            return payload['role']
        except jwt.ExpiredSignatureError:
            # Erreurs d'expiration du token
            pass
        except jwt.InvalidTokenError:
            # Autres erreurs de token
            pass

    return False

def verify_section():
    token = session.get('token')

    if token:
        secret_key = 'fondes2023'
        try:
            payload = jwt.decode(token, secret_key, algorithms=['HS256'])
            return payload['section']
        except jwt.ExpiredSignatureError:
            # Erreurs d'expiration du token
            pass
        except jwt.InvalidTokenError:
            # Autres erreurs de token
            pass

    return False