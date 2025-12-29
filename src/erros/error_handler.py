from src.presentation.http_types.http_response import HttpResponse
from .types import HttpNotFoundError, HttpBadRequestError, HttpUnprocessableEntityError

def handle_errors(error: Exception) -> HttpResponse:
    if isinstance(error, (HttpNotFoundError, HttpBadRequestError, HttpUnprocessableEntityError)):
        return HttpResponse(
            status_code=error.status_code,
            body= {
                "errors": [{
                    "title": error.name,
                    "datail": error.message
                }]
            }
        )
    return HttpResponse(
            status_code=500,
            body= {
                "errors": [{
                    "title": "Server Error",
                    "datail": str(error)
                }]
            }
        )