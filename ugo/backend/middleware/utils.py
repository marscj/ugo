import re
from rest_framework.views import exception_handler
from rest_framework.exceptions import ErrorDetail
from django.utils.six import text_type

def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)

    for key, value in response.data.items():
        if isinstance(object, (list,)):
            response.data[key] = value[0]
        else:
            response.data[key] = value
    
    if response is not None:
        response.data = {
            'message': response.data
        }
    return response 