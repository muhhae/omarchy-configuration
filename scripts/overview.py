#!/usr/bin/env python3
import subprocess
import json

windows = json.loads(
    subprocess.run(
        [
            "hyprctl",
            "clients",
            "-j",
        ],
        capture_output=True,
        text=True,
        check=True,
    ).stdout.strip()
)

ICONS = {
    "firefox": "󰈹",
    "google-chrome": "",
    "chromium": "",
    "zen": "󰈹",
    "cursor": "󰨞",
    "code": "󰨞",
    "Alacritty": "",
    "kitty": "",
    "foot": "",
    "ghostty": "",
    "com.mitchellh.ghostty": "",
    "spotify": "",
    "slack": "",
    "discord": "󰙯",
    "thunar": "󰉋",
    "nautilus": "󰉋",
    "vlc": "󰕼",
}

def get_icon(klass):
    for key, icon in ICONS.items():
        if key in klass.lower():
            return icon
    return "󱂬"

entries = []
addresses = []
for w in windows:
    if not w["mapped"]:
        continue
    
    addresses.append(w["address"])
    title = w["title"]
    klass = w["class"]
    initial_title = w["initialTitle"]
    
    icon = get_icon(klass)
    
    # Elegant format: ICON  InitialTitle  •  WindowTitle
    entry = f"{icon}  {initial_title}  •  {title}"
    entries.append(entry)

res = subprocess.run(
    [
        "walker",
        "--dmenu",
        "--index",
        "-p",
        "Select window:",
    ],
    input="\n".join(entries),
    capture_output=True,
    text=True,
)

if res.returncode == 0 and res.stdout.strip() != "":
    try:
        idx = int(res.stdout.strip())
        selected_address = addresses[idx]
        subprocess.run(
            [
                "hyprctl",
                "dispatch",
                "focuswindow",
                f"address:{selected_address}",
            ],
            check=True,
        )
    except (ValueError, IndexError):
        pass
