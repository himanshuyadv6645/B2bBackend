from rest_framework.views import exception_handler
from rest_framework.response import Response
from rest_framework import status


def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)

    if response is not None:
        error_data = {
            'success': False,
            'error': {
                'status_code': response.status_code,
            }
        }

        if isinstance(response.data, dict):
            error_data['error']['message'] = response.data.get('detail', 'An error occurred')
            error_data['error']['details'] = {
                k: v for k, v in response.data.items() if k != 'detail'
            }
        elif isinstance(response.data, list):
            error_data['error']['message'] = response.data[0] if response.data else 'An error occurred'
            error_data['error']['details'] = {}
        else:
            error_data['error']['message'] = str(response.data)

        response.data = error_data
    else:
        import logging
        logger = logging.getLogger(__name__)
        logger.exception('Unhandled exception: %s', exc)

        response = Response(
            {
                'success': False,
                'error': {
                    'status_code': status.HTTP_500_INTERNAL_SERVER_ERROR,
                    'message': 'Internal server error',
                    'details': {},
                }
            },
            status=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )

    return response
