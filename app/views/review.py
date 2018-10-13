import logging

from app.models.ReviewModel import ReviewModelSchema
from flask import Blueprint, abort, make_response
from flask_api import status
from flask_apispec import doc, marshal_with, use_kwargs
from flask_apispec.views import MethodResource
from app.services.db.ReviewController import ReviewService
from app.util.db_tool import unrequire
from libs.parameters import RequestParams

logger = logging.getLogger(__name__)
app = Blueprint(
    'reviews',
    __name__,
    url_prefix='/reviews'
)
@doc(tags=['Reviews List view'])
class ReviewResourceList(MethodResource):
    review_service = ReviewService()
    @marshal_with(ReviewModelSchema(many=True), code=status.HTTP_200_OK)
    @use_kwargs({
        **RequestParams.pagination_params(),
        **unrequire(ReviewModelSchema().fields)
    })
    @doc(description='return all reviews')
    def get(self, **kwargs):
        page = kwargs.pop('page')
        limit = kwargs.pop('limit')

        return self.review_service.get_multiple(
            page=page,
            limit=limit,
            kwarg_filters=kwargs
        ), status.HTTP_200_OK

    @use_kwargs(ReviewModelSchema().fields)
    @marshal_with(ReviewModelSchema, code=status.HTTP_201_CREATED)
    @doc(description='Create a new review')
    def post(self, **kwargs):
        new_service = self.review_service.create(**kwargs)
        return new_service, status.HTTP_201_CREATED

@doc(tags=['Reviews detail view'])
class ReviewResourceDetail(MethodResource):
    review_service = ReviewService()
    @marshal_with(ReviewModelSchema, code=status.HTTP_200_OK)
    @doc(description='return review with id')
    def get(self, review_id, **kwargs):
        result = self.review_service.get_by_id(review_id)
        if result == None:
            abort(status.HTTP_404_NOT_FOUND)
        return result, status.HTTP_200_OK
    
    @marshal_with(None, code=status.HTTP_204_NO_CONTENT)
    @doc(description='delete a review')
    def delete(self, review_id, **kwargs):
        result = self.review_service.delete_by_id(review_id)
        if result == False:
            abort(status.HTTP_404_NOT_FOUND)
        return make_response('', status.HTTP_204_NO_CONTENT)
    
    @use_kwargs(ReviewModelSchema().fields)
    @marshal_with(ReviewModelSchema, code=status.HTTP_200_OK)
    @doc(description='update a existing review')
    def put(self, review_id, **kwargs):
        result = self.review_service.update_by_id(review_id, kwargs)
        if result == None:
            abort(status.HTTP_404_NOT_FOUND)
        return result, status.HTTP_200_OK

    @use_kwargs(unrequire(ReviewModelSchema().fields))
    @doc(description='partially update a review')
    @marshal_with(ReviewModelSchema, code=status.HTTP_200_OK)
    def patch(self, review_id, **kwargs):
        result = self.review_service.update_by_id(review_id, kwargs)
        if result == None:
            abort(status.HTTP_404_NOT_FOUND)
        return result, status.HTTP_200_OK

app.add_url_rule(
    '',
    view_func=ReviewResourceList.as_view('ReviewResourceList'),
    methods=['GET', 'POST']
)
app.add_url_rule(
    '/<int:review_id>',
    view_func=ReviewResourceDetail.as_view('ReviewResourceDetail'),
    methods=['GET', 'PUT', 'DELETE', 'PATCH']
)
