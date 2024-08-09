from rest_framework.exceptions import APIException
from rest_framework.response import Response


success = Response({'detail': "Success!"}, 200)


response_schema = {
    200: {"description": "The operation was completed successfully", "example": {"detail": "Success!"}},
    # 400: {"description": "The operation did not complete successfully", "example": {"response": "Bad Request!"}},
}
