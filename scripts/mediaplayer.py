#!/usr/bin/python3

import subprocess
import time
import sys
import json
import html


def get_player_data():
    try:
        data = subprocess.run(
            [
                "playerctl",
                "-p",
                "spotify,%any",
                "metadata",
                "--format",
                '{ "status": "{{status}}", "title": "{{title}}", "artist": "{{artist}}", "length": {{mpris:length}}, "position": {{position}}, "volume": {{volume}} }',
            ],
            capture_output=True,
            text=True,
        )
        # print(data.args)
        j = data.stdout.strip()
        metadata = json.loads(j)
        return metadata

    except Exception:
        return None


bar_len = 10

fill_char_passed = "━"
fill_char_progress = "─"
indicator = "●"

# fill_char_passed = "█"
# fill_char_progress = "░"
# indicator = "█"

border_left = "⟦"
border_right = "⟧"

border_left = "("
border_right = ")"

border_left = ""
border_right = ""

icon = ""
icon = ""

# "format": "   {title} - {artist}",
# "format-paused": " ⏸  {title} - {artist}",


while True:
    data = get_player_data()

    if data:
        if data.get("length", 0) > 0:
            pct = min(1.0, max(0.0, data["position"] / data["length"]))
        else:
            pct = 0

        spot_to_fill = bar_len - 1
        filled_count = round(pct * spot_to_fill)
        empty_count = spot_to_fill - filled_count

        output = {}
        status = icon if data["status"] == "Playing" else "⏸"
        progress_bar = (
            border_left
            + fill_char_passed * filled_count
            + indicator
            + fill_char_progress * empty_count
            + border_right
        )
        position_str = time.strftime("%M:%S", time.gmtime(data["position"] / 1_000_000))
        length_str = time.strftime("%M:%S", time.gmtime(data["length"] / 1_000_000))

        output["text"] = html.escape(
            f" {status}  {position_str} {progress_bar} {length_str}  {data['title']} - {data['artist']}"
        )
        output["tooltip"] = (
            "left-click: play/pause\n"
            + "right-click: next song\n"
            + "middle-click: previous song\n"
            + "scroll: volume+/-"
        )
        print(f"{json.dumps(output, ensure_ascii=False)}")
    else:
        print("No Player")

    sys.stdout.flush()
    time.sleep(1)
