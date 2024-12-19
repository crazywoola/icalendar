from collections.abc import Generator
import datetime
from typing import Any
import uuid

from dify_plugin import Tool
from dify_plugin.entities.tool import ToolInvokeMessage

class CalendarTool(Tool):
    def _invoke(self, tool_parameters: dict[str, Any]) -> Generator[ToolInvokeMessage]:
        dtstart = tool_parameters.get("dtstart", )
        dtend = tool_parameters.get("dtend")
        summary = tool_parameters.get("summary")
        description = tool_parameters.get("description")
        location = tool_parameters.get("location")
        rrule = tool_parameters.get("rrule")
        attendees = tool_parameters.get("attendees")

        uid = uuid.uuid4().hex
        dtstamp = datetime.datetime.now().strftime("%Y%m%dT%H%M%SZ")
        ics_content = f"""BEGIN:VCALENDAR
VERSION:2.0
BEGIN:VEVENT
UID:{uid}
DTSTAMP:{dtstamp}
DTSTART:{dtstart}
DTEND:{dtend}
SUMMARY:{summary}
DESCRIPTION:{description}
LOCATION:{location}
RRULE:{rrule}
ATTENDEE:{attendees}
END:VEVENT
END:VCALENDAR"""
        self.session.storage.set(uid, ics_content.encode("utf-8"))
        yield self.create_json_message({
            "result": {
                "uid": uid,
            },
        })
