from .models import HttpRequestLogEntry
from datetime import datetime


class HttpRequestDbLoggingMiddleware(object):

    """Middleware, that stores http requests in the db"""

    def process_request(self, request):

        logentry = HttpRequestLogEntry(
            date=datetime.now(),
            request_method=request.META.get('REQUEST_METHOD', '?'),
            path=request.path[:256]
        )

        logentry.save()
