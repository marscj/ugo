from rest_framework.views import exception_handler

def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)

    if response is not None and response.data is not None:
        for key, value in response.data.items():
            if isinstance(value, (list,)):
                response.data[key] = value[0]
            else:
                if isinstance(value, (dict,)):
                    for _key, _value in value.items():
                        response.data[key] = _value[0]
                else:
                    response.data[key] = value
                    
        response.data = {
            'message': response.data
        }
    
    return response 