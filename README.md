## Calendar

**Author:** crazywoola
**Version:** 0.0.1
**Type:** extension

### Description

UID：事件的唯一标识符。
DTSTAMP：事件的创建或最后修改时间。
DTSTART 和 DTEND：事件的开始和结束时间。
SUMMARY：事件标题。
DESCRIPTION：事件的详细说明。
LOCATION：事件地点。
RRULE：重复规则（如 FREQ=DAILY;INTERVAL=1 表示每天重复一次）。
ATTENDEE：参与者的电子邮件。

# calendar_id = self.session.storage.get("calendar_id").decode('utf-8')
# self.session.storage.set("calendar_id", "123").encode('utf-8')

