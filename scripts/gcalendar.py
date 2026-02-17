#!/usr/bin/python3

from datetime import date
from datetime import datetime
import html
import json
import subprocess
import time
import sys
import pandas as pd
import io

title_max_len = 24
icon = " "
while True:
    out = {}
    try:
        gcalcli = subprocess.run(
            [
                "/usr/bin/gcalcli",
                "agenda",
                "--tsv",
            ],
            capture_output=True,
            text=True,
            check=True,
        ).stdout.strip()

        events = pd.read_csv(io.StringIO(gcalcli), delimiter="\t")
        print(events)

        today = date.today().isoformat()

        events["dt_end"] = pd.to_datetime(events["end_date"] + " " + events["end_time"])
        now = datetime.now()

        today_events = events.query("start_date == @today and dt_end > @now")
        upcoming_events = events.query("dt_end > @now or dt_end.isna()")

        if today_events.empty:
            text = "No events today!"
        else:
            closest_event = today_events.iloc[0]

            start_time = (
                datetime.strptime(closest_event["start_time"], "%H:%M")
                .strftime("%I:%M %p")
                .lstrip("0")
            )
            end_time = (
                datetime.strptime(closest_event["end_time"], "%H:%M")
                .strftime("%I:%M %p")
                .lstrip("0")
            )

            title = closest_event["title"]
            title = (
                (title[: title_max_len - 3] + "...")
                if len(title) > title_max_len
                else title
            )

            text = f"{title} at {start_time} - {end_time}"

        if upcoming_events.empty:
            tooltip = "No upcoming events"
        else:
            tooltip = []
            current_date = ""
            for event in upcoming_events.itertuples():
                if current_date != event.start_date:
                    current_date = event.start_date
                    formatted = datetime.strptime(
                        current_date,
                        "%Y-%m-%d",
                    ).strftime("%b %-d")
                    tooltip.append(f"<b>{formatted}</b>")
                event_date = (
                    f"{event.start_time} - {event.end_time}"
                    if pd.notna(event.end_time)
                    else "All day"
                )
                tooltip.append(f"  {event_date:<{13}} {html.escape(event.title)}")
            tooltip = "\n".join(tooltip)

    except Exception:
        text = f"Err: {Exception}"
        tooltip = f"Err: {Exception}"

    out["text"] = html.escape(f"{icon} {text}")
    out["tooltip"] = tooltip
    print(json.dumps(out, ensure_ascii=False))
    sys.stdout.flush()
    time.sleep(300)
    # time.sleep(1)
