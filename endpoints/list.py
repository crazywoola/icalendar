from typing import Mapping
from werkzeug import Request, Response
from dify_plugin import Endpoint

class ListEndpoint(Endpoint):
    def _invoke(self, r: Request, values: Mapping, settings: Mapping) -> Response:
        """
        Invokes the endpoint with the given request.
        """
        print(r.base_url)
        try:
            list = self.session.storage.get('list').decode("utf-8").split('|')
        except AttributeError:
            list = []
        html = f"""<html>
<head>
    <title>Events List</title>
</head>
<body>
    <h1>Events List</h1>
    <ul>
        {"".join([f"<li>{event}</li>" for event in list])}
    </ul>
</body>
</html>"""
        return Response(html, status=200, content_type="text/html")
