from rest_framework.response import Response
from rest_framework import status


def success_response(data=None, message='Success', status_code=status.HTTP_200_OK):
    response_data = {
        'success': True,
        'message': message,
    }
    if data is not None:
        response_data['data'] = data
    return Response(response_data, status=status_code)


def created_response(data=None, message='Created successfully'):
    return success_response(data=data, message=message, status_code=status.HTTP_201_CREATED)


def no_content_response(message='Deleted successfully'):
    return Response(
        {'success': True, 'message': message},
        status=status.HTTP_204_NO_CONTENT,
    )


def bad_request_response(message='Bad request', errors=None):
    response_data = {
        'success': False,
        'message': message,
    }
    if errors:
        response_data['errors'] = errors
    return Response(response_data, status=status.HTTP_400_BAD_REQUEST)


def not_found_response(message='Resource not found'):
    return Response(
        {'success': False, 'message': message},
        status=status.HTTP_404_NOT_FOUND,
    )


def forbidden_response(message='Permission denied'):
    return Response(
        {'success': False, 'message': message},
        status=status.HTTP_403_FORBIDDEN,
    )


def unauthorized_response(message='Authentication required'):
    return Response(
        {'success': False, 'message': message},
        status=status.HTTP_401_UNAUTHORIZED,
    )
