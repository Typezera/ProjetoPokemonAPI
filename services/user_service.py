from models import db   
from dtos.user_request_dto import UserRequestDto
from dtos.user_response_dto import UserResponseDTO
from security.jwt_util import JwtUtil
from entities.user_entity import User
#from dtos.user_login_response_dto import UserLoginResponseDTO
from dtos.user_login_request_dto import UserLoginRequestDTO
from dtos.user_login_response_dto import UserLoginResponseDTO


class UserService:
    @staticmethod
    def create_user(data):
        #"make the new user in DB"
        try:
           user_dto = UserRequestDto(data)

           if not user_dto.is_valid():
               return {"sucess": False, "error": "Required fields are missing"}
           
           new_user = user_dto.to_entity()
           db.session.add(new_user)
           db.session.commit()

           response = UserResponseDTO.from_entity(new_user)
           return {"sucess": True, "user": response}
        except Exception as e:
            db.session.rollback()
            return {"sucess": False, "error": str(e)}
        
    @staticmethod
    def get_all_users():
        users = db.session.query("User").all()
        data = UserResponseDTO.from_entity_list(users)
        return {"sucess": True, "users": data} 

    @staticmethod
    def login_user(data):
        try:
            login_dto = UserLoginRequestDTO(
                email=data.get('email'),
                password=data.get('password')
            )

            if not login_dto.email or not login_dto.password:
                return {"success": False, "error": "Email and password are required"}, 400
            
            user = User.query.filter_by(email=login_dto.email).first()
            if not user or not user.check_password(login_dto.password):
                return {"success": False, "error": "Invalid credentials"}, 401

            token = JwtUtil.generate_token(user.id)
            
            response_dto = UserLoginResponseDTO(
                id=user.id,
                name=user.name,
                email=user.email,
                jwt=token
            )

            return {"success": True, "user": response_dto.to_dict()}, 200
        
        except Exception as e:
            return {"success": False, "error": str(e)}, 500
