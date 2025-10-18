class UserLoginResponseDTO:
    def __init__(self, id, name, email, jwt):
        self.id = id
        self.name = name
        self.email = email
        self.jwt = jwt

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email,
            "jwt": self.jwt
        }
        