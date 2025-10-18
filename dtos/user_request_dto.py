class UserRequestDto:
    # This DTO is used to create a user, everything that is mandatory for the user to enter.

    def __init__(self, data):
        self.name = data.get('name')
        self.email = data.get('email')
        self.password = data.get('password')

    def is_valid(self):
        #validates whether the mandatory fields are filled in   
        return all([self.name, self.email, self.password])
    
    def  to_entity(self):
        from entities.user_entity import User
        user = User(name=self.name, email=self.email)
        user.set_password(self.password)
        return user