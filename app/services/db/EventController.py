from app.models.EventModel import EventModel
from app.services.db.BaseController import BaseService

class EventService(BaseService):
    model = EventModel