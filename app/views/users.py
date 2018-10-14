import logging

from app.models.UserModel import UserModelSchema, UserServiceSchema, UserEventSchema, UserReviewSchema
from flask import Blueprint, abort, make_response
from flask_api import status
from flask_apispec import doc, marshal_with, use_kwargs
from flask_apispec.views import MethodResource
from app.services.db.UserController import UserService
from app.services.db.UserEventController import UserEventService
from app.models.ReviewModel import ReviewModel
from app.models.UserEventRelationModel import UserEventRelationModel
from app.models.UserServiceRelationModel import UserServiceRelationModel
from app.services.db.EventController import EventService
from app.services.db.ReviewController import ReviewService
from app.services.db.ServiceController import ServiceService
from app.models.EventModel import EventModel
from app.util.db_tool import unrequire
from libs.parameters import RequestParams
from libs.security import get_token_info

logger = logging.getLogger(__name__)
app = Blueprint(
    'users',
    __name__,
    url_prefix='/api/users'
)


@doc(tags=['Users List view'])
class UserResourceList(MethodResource):
    user_service = UserService()

    @marshal_with(UserModelSchema(many=True), code=status.HTTP_200_OK)
    @use_kwargs({
        **RequestParams.pagination_params(),
        **unrequire(UserModelSchema().fields)
    })
    @doc(description='return all users')
    def get(self, **kwargs):
        _ = get_token_info()
        page = kwargs.pop('page')
        limit = kwargs.pop('limit')

        return self.user_service.get_multiple(
            page=page,
            limit=limit,
            kwarg_filters=kwargs
        ), status.HTTP_200_OK

    @use_kwargs(UserModelSchema().fields)
    @marshal_with(UserModelSchema, code=status.HTTP_201_CREATED)
    @doc(description='Create a new user')
    def post(self, **kwargs):
        _ = get_token_info()
        new_user = self.user_service.create(**kwargs)
        return new_user, status.HTTP_201_CREATED


@doc(tags=['Nearest Users List view'])
class UsersNearbyResourceList(MethodResource):
    user_service = UserService()

    @marshal_with(UserModelSchema(many=True), code=status.HTTP_200_OK)
    @use_kwargs({
        **RequestParams.pagination_params(),
        **unrequire(UserModelSchema().fields)
    })
    @doc(description='return all nearby guides')
    def get(self, **kwargs):
        uid = kwargs.pop('uid')
        page = kwargs.pop('page')
        limit = kwargs.pop('limit')

        return self.user_service.get_multiple_nearby(
            uid=uid,
        ), status.HTTP_200_OK

@doc(tags=['Events associate with user'])
class UserEventResourceList(MethodResource):
    user_event_service = UserEventService()
    event_service = EventService()

    @marshal_with(UserEventSchema(many=True), code=status.HTTP_200_OK)
    @use_kwargs({
        **RequestParams.pagination_params(),
        **unrequire(UserModelSchema().fields)
    })
    @doc(description='return all events associate with a user')
    def get(self, user_id, **kwargs):
        event_ids = UserEventRelationModel.query.filter(UserEventRelationModel.user_id == user_id).all()
        result = []
        for event in event_ids:
            model = self.event_service.get_by_id(event.event_id)
            result.append(model)
        return result, status.HTTP_200_OK

@doc(tags=['Reviews associate with user'])
class UserReviewResourceList(MethodResource):
    user_event_service = UserEventService()
    review_service = ReviewService()

    @marshal_with(UserReviewSchema(many=True), code=status.HTTP_200_OK)
    @use_kwargs({
        **RequestParams.pagination_params(),
        **unrequire(UserModelSchema().fields)
    })
    @doc(description='return all reviews associate with a user')
    def get(self, user_id, **kwargs):
        review_ids = ReviewModel.query.filter(ReviewModel.user_id == user_id).all()
        result = []
        for review in review_ids:
            model = self.review_service.get_by_id(review.id)
            result.append(model)
        return result, status.HTTP_200_OK

@doc(tags=['Services associate with a user'])
class UserServiceResourceList(MethodResource):
    service_service = ServiceService()

    @marshal_with(UserServiceSchema(many=True), code=status.HTTP_200_OK)
    @use_kwargs({
        **RequestParams.pagination_params(),
        **unrequire(UserModelSchema().fields)
    })
    @doc(description='return all reviews associate with a user')
    def get(self, user_id, **kwargs):
        service_ids = UserServiceRelationModel.query.filter(UserServiceRelationModel.user_id == user_id).all()
        result = []
        for service in service_ids: 
            model = self.service_service.get_by_id(service.service_id)
            model.is_expert = service.is_expert
            result.append(model)
        return result, status.HTTP_200_OK

@doc(tags=['Users detail view'])
class UserResourceDetail(MethodResource):
    user_service = UserService()

    @marshal_with(UserModelSchema, code=status.HTTP_200_OK)
    @doc(description='return user with id')
    def get(self, user_id, **kwargs):
        _ = get_token_info()
        result = self.user_service.get_by_id(user_id)
        if result == None:
            abort(status.HTTP_404_NOT_FOUND)
        return result, status.HTTP_200_OK

    @marshal_with(None, code=status.HTTP_204_NO_CONTENT)
    @doc(description='delete a user')
    def delete(self, user_id, **kwargs):
        _ = get_token_info()
        result = self.user_service.delete_by_id(user_id)
        if result == False:
            abort(status.HTTP_404_NOT_FOUND)
        return make_response('', status.HTTP_204_NO_CONTENT)

    @use_kwargs(UserModelSchema().fields)
    @marshal_with(UserModelSchema, code=status.HTTP_200_OK)
    @doc(description='update a existing user')
    def put(self, user_id, **kwargs):
        _ = get_token_info()
        result = self.user_service.update_by_id(user_id, kwargs)
        if result == None:
            abort(status.HTTP_404_NOT_FOUND)
        return result, status.HTTP_200_OK

    @use_kwargs(unrequire(UserModelSchema().fields))
    @doc(description='partially update a recurring frequency')
    @marshal_with(UserModelSchema, code=status.HTTP_200_OK)
    def patch(self, user_id, **kwargs):
        _ = get_token_info()
        result = self.user_service.update_by_id(user_id, kwargs)
        if result == None:
            abort(status.HTTP_404_NOT_FOUND)
        return result, status.HTTP_200_OK


app.add_url_rule(
    '',
    view_func=UserResourceList.as_view('UserResourceList'),
    methods=['GET', 'POST']
)
app.add_url_rule(
    '/nearest/<int:uid>',
    view_func=UsersNearbyResourceList.as_view('UsersNearbyResourceList'),
    methods=['GET', 'POST']
)
app.add_url_rule(
    '/<int:user_id>',
    view_func=UserResourceDetail.as_view('UserResourceDetail'),
    methods=['GET', 'PUT', 'DELETE', 'PATCH']
)
app.add_url_rule(
    '/<int:user_id>/events',
    view_func=UserEventResourceList.as_view('UserEventResourceList'),
    methods=['GET']
)
app.add_url_rule(
    '/<int:user_id>/reviews',
    view_func=UserReviewResourceList.as_view('UserReviewResourceList'),
    methods=['GET']
)
app.add_url_rule(
    '/<int:user_id>/services',
    view_func=UserServiceResourceList.as_view('UserServiceResourceList'),
    methods=['GET']
)
