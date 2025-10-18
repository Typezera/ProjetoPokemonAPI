class UserResponseDTO:
    ##DTO responsible for the response the user will receive creating the account

    @staticmethod
    def from_entity(user, jwt=None):
        #try converts the user entity to a dictionary
        return {
            "id": user.id,
            "name": user.name,
            "email": user.email,
        }
    
    @staticmethod
    def from_entity_list(users):
        return [UserResponseDTO.from_entity(user) for user in users]
    