-- Keymaps are automatically loaded on the VeryLazy event
-- Default keymaps that are always set: https://github.com/LazyVim/LazyVim/blob/main/lua/lazyvim/config/keymaps.lua
-- Add any additional keymaps here

vim.keymap.set({ "n", "v" }, "d", '"_d')
vim.keymap.set("n", "dd", '"_dd')

vim.keymap.set("n", "<C-f>", [[:%s~~~gI<left><Left><Left><Left>]])
vim.keymap.set("x", "<C-f>", [[:s~~~gI<left><Left><Left><Left>]])

vim.keymap.set("n", "vw", "viw", { desc = "Select current word" })
vim.keymap.set("n", "vW", "viW", { desc = "Select current WORD" })
vim.keymap.set("n", "vs", "viws", { desc = "Select current word and replace" })

vim.keymap.set({ "i", "v" }, "<C-c>", "<Esc>")
