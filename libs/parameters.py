import marshmallow
from marshmallow import validate


class RequestParams:
    pagination_default_limit = 10
    pagination_default_page = 1

    @staticmethod
    def pagination_params(
        limit=pagination_default_limit,
        page=pagination_default_page
    ):
        """
        Return dict of limit and page fields and their validators for use_kwargs
        :param limit:
        :param page:
        :return:
        """
        return {
            'limit': marshmallow.fields.Integer(missing=limit, validate=validate.Range(min=1)),
            'page': marshmallow.fields.Integer(missing=page, validate=validate.Range(min=page))
        }
