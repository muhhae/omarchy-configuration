#!/usr/bin/env python3
import subprocess
from collections import defaultdict
import json

icons = {
    "Slack": "",
}

all_workspaces = json.loads(
    subprocess.run(
        [
            "hyprctl",
            "workspaces",
            "-j",
        ],
        capture_output=True,
        text=True,
        check=True,
    ).stdout.strip()
)
max_id = max([w["id"] for w in all_workspaces])

active_workspace = json.loads(
    subprocess.run(
        [
            "hyprctl",
            "activeworkspace",
            "-j",
        ],
        capture_output=True,
        text=True,
        check=True,
    ).stdout.strip()
)

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

max_title_length = 16
workspaces = [[] for _ in range(max_id)]
for w in windows:
    w_id = w["workspace"]["id"] - 1
    title = w["initialTitle"]
    # title = w[""]
    if len(title) > max_title_length:
        title = title[: max_title_length - 3] + "..."
    workspaces[w_id].append(title)

active_workspace_id = int(active_workspace["id"])
print(active_workspace_id)
entries = [
    f"{k + 1}: {', '.join(v) if len(v) > 0 else '(empty)'}"
    for k, v in enumerate(workspaces)
    # if k + 1 != active_workspace_id
]

selected = subprocess.run(
    [
        "walker",
        "--dmenu",
        "-p",
        "Select workspace:",
        # "-q",
        # "-c",
        # "3",
    ],
    input="\n".join(entries),
    capture_output=True,
    text=True,
    check=True,
).stdout.strip()

if selected != "":
    selected_window = selected[: selected.find(":")]
    subprocess.run(
        [
            "hyprctl",
            "dispatch",
            "workspace",
            selected_window,
        ]
    )
