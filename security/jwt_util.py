import jwt
import datetime
import os
from dotenv import load_dotenv

load_dotenv()
SECRET_KEY = os.getenv('SECRET_KEY')

class JwtUtil:
    @staticmethod
    def generate_token(user_id, email=None):
        ##Genereted a JWT valid for 24h
        payload = {
            'user_id': user_id,
            'email': email,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(days=24),
        }
        token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')
        return token
    
    @staticmethod
    def verify_token(token): #verify and decode JWT
        try:
            decoded = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
            return {"valid": True, "data": decoded}
        except jwt.ExpiredSignatureError:
            return {"valid": False, "message": "Token expired"}
        except jwt.InvalidTokenError:
            return {"valid": False, "Error": "Invalid token"}
        
