# pylint: disable=missing-class-docstring
from enum import Enum


class RequestType(Enum):
    GET = "GET"
    POST = "POST"
    PUT = "PUT"
    DELETE = "DELETE"
