import time
from typing import Mapping
from werkzeug import Request, Response
from dify_plugin import Endpoint


class CalendarEndpoint(Endpoint):
    def _invoke(self, r: Request, values: Mapping, settings: Mapping) -> Response:
        """
        Invokes the endpoint with the given request.
        """
        calendar_id = values.get("calendar_id")
        
        def generator():
            try:
                ics_content = self.session.storage.get(calendar_id).decode('utf-8')
                yield ics_content
            except:
                yield f"Calendar with id {calendar_id} not found"
                return
        return Response(generator(), status=200, content_type="text/plain")
