from rest_framework.views import exception_handler

def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)

    for key, value in response.data.items():
        if isinstance(value, (list,)):
            response.data[key] = value[0]
        else:
            response.data[key] = value
    
    if response is not None:
        response.data = {
            'message': response.data
        }

    print(response.data)
    return response 