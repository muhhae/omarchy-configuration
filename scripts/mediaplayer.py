#!/usr/bin/python3

from os import abort
import subprocess
import time
import sys
import json
import html


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


playerctl = subprocess.Popen(
    [
        "playerctl",
        "-p",
        "spotify,%any",
        "metadata",
        "--format",
        "{{status}}|{{title}}|{{artist}}|{{mpris:length}}|{{position}}|{{volume}}",
        "--follow",
    ],
    stdout=subprocess.PIPE,
    text=True,
)

for line in playerctl.stdout:
    parts = line.split("|")
    metadata = {
        "status": parts[0],
        "title": parts[1],
        "artist": parts[2],
        "length": int(parts[3]) if parts[3] else 0,
        "position": int(parts[4]) if parts[4] else 0,
        "volume": float(parts[5]) if parts[5] else 0.0,
    }
    if metadata.get("length", 0) > 0:
        pct = min(1.0, max(0.0, metadata["position"] / metadata["length"]))
    else:
        pct = 0

    spot_to_fill = bar_len - 1
    filled_count = round(pct * spot_to_fill)
    empty_count = spot_to_fill - filled_count

    status = icon if metadata["status"] == "Playing" else "⏸"
    progress_bar = (
        border_left
        + fill_char_passed * filled_count
        + indicator
        + fill_char_progress * empty_count
        + border_right
    )
    position_str = time.strftime("%M:%S", time.gmtime(metadata["position"] / 1_000_000))
    length_str = time.strftime("%M:%S", time.gmtime(metadata["length"] / 1_000_000))

    output = {}
    output["text"] = html.escape(
        f" {status}  {position_str} {progress_bar} {length_str}  {metadata['title']} - {metadata['artist']}"
    )
    output["tooltip"] = (
        f"Artist: {metadata['artist']}\n"
        + f"Title: {metadata['title']}\n\n"
        + "left-click: play/pause\n"
        + "right-click: next song\n"
        + "middle-click: previous song\n"
        + "scroll: volume+/-"
    )

    print(f"{json.dumps(output, ensure_ascii=False)}")
    sys.stdout.flush()
