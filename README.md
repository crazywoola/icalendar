## Calendar

**Author:** crazywoola
**Version:** 0.0.1
**Type:** extension

### Description

This extension allows the user to interact with their Google Calendar. 

### ICS Format

```
UID: The unique identifier for the event.
DTSTAMP: The timestamp of when the event was created or last modified.
DTSTART and DTEND: The start and end times of the event.
SUMMARY: The title of the event.
DESCRIPTION: A detailed description of the event.
LOCATION: The location of the event.
RRULE: The recurrence rule (e.g., FREQ=DAILY;INTERVAL=1 means the event repeats daily).
ATTENDEE: The email addresses of the participants.
```

How to save the things in the storage:

```python
# Example usage:
calendar_id = self.session.storage.get("calendar_id").decode('utf-8')
self.session.storage.set("calendar_id", "123").encode('utf-8')
```

