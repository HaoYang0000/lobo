import datetime
import logging

import jwt
from flask import request, abort
from flask_api import status
from jwt.exceptions import (
    InvalidTokenError, DecodeError, InvalidSignatureError,
    ExpiredSignatureError, InvalidAudienceError, InvalidIssuerError,
    InvalidIssuedAtError, ImmatureSignatureError, InvalidKeyError,
    InvalidAlgorithmError, MissingRequiredClaimError
)

logger = logging.getLogger('flask.app')


HEADER_PREFIX = "bearer"


class JWTConfig:
    jwt_secret = 'my_precious'
    jwt_algo = 'HS256'
    jwt_exp_seconds = 604800  # 7 days

    def __init__(self):
        pass


def parse_token(token, abort_if_invalid=True):
    try:
        decoded = jwt.decode(token, JWTConfig.jwt_secret, algorithms=JWTConfig.jwt_algo)
        return decoded
    except (
        InvalidTokenError, DecodeError, InvalidSignatureError,
        ExpiredSignatureError, InvalidAudienceError, InvalidIssuerError,
        InvalidIssuedAtError, ImmatureSignatureError, InvalidKeyError,
        InvalidAlgorithmError, MissingRequiredClaimError
    ) as e:
        logging.exception(e)
        if abort_if_invalid:
            abort(status.HTTP_401_UNAUTHORIZED)
        else:
            raise


def create_token(*, user_id=None):
    payload = {
        "sub": user_id,
        "exp": datetime.datetime.utcnow() + datetime.timedelta(seconds=JWTConfig.jwt_exp_seconds),
        "iat": datetime.datetime.utcnow()
    }
    return jwt.encode(payload, JWTConfig.jwt_secret, algorithm=JWTConfig.jwt_algo).decode("utf-8")


def _verify_auth_header(auth_header):
    auth_parts = auth_header.split()
    auth_len = len(auth_parts)
    if auth_len != 2:
        raise ValueError("Invalid JWT header - Length")
    if auth_parts[0].lower() != HEADER_PREFIX:
        raise ValueError("JWT header should have a '{prefix}' prefix".format(prefix=HEADER_PREFIX))
    return auth_parts[1]


def jwt_check(auth_header):
    token = _verify_auth_header(auth_header)
    return parse_token(token)


def get_token_info():
    """
    Extracts user info from bearer token
    """
    auth_header = request.headers.get("Authorization", '')
    try:
        return jwt_check(auth_header)
    except ValueError:
        abort(status.HTTP_401_UNAUTHORIZED)
