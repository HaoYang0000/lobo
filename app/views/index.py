from flask import Blueprint
import json
import logging


app = Blueprint('index', __name__)
logger = logging.getLogger(__name__)


def decode_incoming_request(request):
    """
    Basic validation of incoming request
    Checks if we have a valid json request

    Args:
        request (obj): Request object from Flask

    Returns:
        dict. The JSON decoded request

    Raises:
        Exception: We are missing data
        json.decoder.JSONDecodeError: Invalid JSON
    """
    logger.info("request: '{}'".format(request.data))

    data = request.data

    if len(data) == 0:
        raise Exception("empty request")

    message = json.loads(data)

    return message


@app.route('/health', methods=['GET', 'POST'])
def health():
    """
    Health route for OPS monitoring
    :return: (tuple) 'OK', HTTP 200 Response
    """
    return 'OK', 200


@app.route('/', methods=['GET', 'POST'])
def index():
    """
    Stub for index route
    """
    return "It's alive!"
