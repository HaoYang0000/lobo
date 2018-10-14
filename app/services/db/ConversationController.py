from app.models.Conversation import ConversationModel
from app.services.db.BaseController import BaseService

class ConversationService(BaseService):
    model = ConversationModel