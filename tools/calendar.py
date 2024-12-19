from collections.abc import Generator
import datetime
from typing import Any
import uuid

from dify_plugin import Tool
from dify_plugin.entities.tool import ToolInvokeMessage

class CalendarTool(Tool):
    def _invoke(self, tool_parameters: dict[str, Any]) -> Generator[ToolInvokeMessage]:
        dtstart = tool_parameters.get("dtstart")
        dtend = tool_parameters.get("dtend")
        summary = tool_parameters.get("summary")
        description = tool_parameters.get("description")
        location = tool_parameters.get("location")
        rrule = tool_parameters.get("rrule")
        attendees = tool_parameters.get("attendees")

        # Validate required parameters
        if not all(isinstance(param, str) for param in [dtstart, dtend, summary]):
            raise ValueError("'dtstart', 'dtend', and 'summary' must be provided as strings.")
        
        # Validate dtstart and dtend format
        try:
            dtstart = datetime.datetime.strptime(dtstart, "%Y-%m-%dT%H:%M:%S").strftime("%Y%m%dT%H%M%SZ")
            dtend = datetime.datetime.strptime(dtend, "%Y-%m-%dT%H:%M:%S").strftime("%Y%m%dT%H%M%SZ")
        except ValueError:
            raise ValueError("'dtstart' and 'dtend' must be in the format 'YYYY-MM-DDTHH:MM:SS' and in UTC.")

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
STATUS:CONFIRMED
END:VEVENT
END:VCALENDAR"""
        self.session.storage.set(uid, ics_content.encode("utf-8"))

        # Add uid to list
        try:
            list = self.session.storage.get('list').decode("utf-8").split('|')
        except:
            list = []
        list.append(uid)
        self.session.storage.set('list', "|".join(list).encode("utf-8"))
        yield self.create_json_message({
            "result": {
                "uid": uid,
            },
        })
        yield self.create_text_message(uid)