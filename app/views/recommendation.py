import logging

from flask import Blueprint, abort, make_response
from flask.json import jsonify
from flask_api import status
from flask_apispec import doc, marshal_with, use_kwargs
from flask_apispec.views import MethodResource
from marshmallow import fields
from recombee_api_client.api_client import RecombeeClient
from recombee_api_client.api_requests import AddPurchase, RecommendItemsToUser, Batch

from libs.security import get_token_info

logger = logging.getLogger(__name__)
app = Blueprint(
    'recommendation',
    __name__,
    url_prefix='/api/recommendations'
)


class Recommendation(MethodResource):

    @use_kwargs({
        'user_id': fields.Integer(),
        'service_id': fields.Integer()
    })
    @marshal_with(None, code=status.HTTP_200_OK)
    @doc(description='send recommendation record to Recombee')
    def post(self, user_id, service_id):
        _ = get_token_info()
        client = RecombeeClient('globalhack', 'QluRxG1ZkI3kRKvukeXpscV4kRcTxIPAIYbxVjlD14FJlhS0rLdVYVxv25NNeBYC')
        request = AddPurchase(user_id, service_id, cascade_create=True)
        purchase_requests = [request]
        try:
            # Send the data to Recombee, use Batch for faster processing of larger data
            response = client.send(Batch(purchase_requests))
            return make_response(jsonify(response))
        except Exception:
            abort(status.HTTP_500_INTERNAL_SERVER_ERROR)

    @use_kwargs({
        'user_id': fields.Integer()
    })
    @marshal_with(None, code=status.HTTP_200_OK)
    @doc(description='get recommendation for a certain user from Recombee')
    def get(self, user_id):
        _ = get_token_info()
        client = RecombeeClient('globalhack', 'QluRxG1ZkI3kRKvukeXpscV4kRcTxIPAIYbxVjlD14FJlhS0rLdVYVxv25NNeBYC')
        try:
            # get the recommendation
            response = client.send(RecommendItemsToUser(user_id, 5))
            return make_response(jsonify(response))
        except Exception:
            abort(status.HTTP_500_INTERNAL_SERVER_ERROR)


app.add_url_rule(
    '',
    view_func=Recommendation.as_view('Recommendation'),
    methods=['GET', 'POST']
)
