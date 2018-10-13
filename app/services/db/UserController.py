from app.models.UserModel import UserModel
from app.services.db.BaseController import BaseService

class UserService(BaseService):
    model = UserModel