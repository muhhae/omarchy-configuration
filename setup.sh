#!/usr/bin/env zsh
set -x

base_dir="${0:a:h}"

typeset -A items
items=(
    ["zsh"]="$HOME/.config/zsh"
    ["nvim"]="$HOME/.config/nvim"
    ["tmux"]="$HOME/.config/tmux"
    ["ghostty"]="$HOME/.config/ghostty"
    ["waybar"]="$HOME/.config/waybar"
    ["starship.toml"]="$HOME/.config/starship.toml"
    ["hypr"]="$HOME/.config/hypr"
    ["tmux"]="$HOME/.config/tmux"
    ["lazygit"]="$HOME/.config/lazygit"
)

for src_name dest in ${(kv)items}; do
    src_path="$base_dir/$src_name"

    mkdir -pv "${dest:h}"

    rm -rf "$dest"

    # -s: symbolic
    # -v: verbose
    # -f: force (removes existing file)
    # -n: treat destination as a normal file if it is a symlink to a directory
    ln -svfn "$src_path" "$dest"
done
