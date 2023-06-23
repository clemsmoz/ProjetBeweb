from flask import session
import jwt

def has_valid_token():
    token = session.get('token')

    if token:
        secret_key = 'fondes2023'

        try:
            payload = jwt.decode(token, secret_key, algorithms=['HS256'])
            # Vérifiez les informations supplémentaires dans le payload si nécessaire
<<<<<<< HEAD
<<<<<<< HEAD
            return payload['role']
=======
            return payload['user_type']
>>>>>>> origin/test
=======
            return payload['role']
>>>>>>> 706f18afd9c9d68616a44f9f73cec89ac68481aa
        except jwt.ExpiredSignatureError:
            # Gérer les erreurs d'expiration du token
            pass
        except jwt.InvalidTokenError:
            # Gérer les autres erreurs de token
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
            # Gérer les erreurs d'expiration du token
            pass
        except jwt.InvalidTokenError:
            # Gérer les autres erreurs de token
            pass

    return False