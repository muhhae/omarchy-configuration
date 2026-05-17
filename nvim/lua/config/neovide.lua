if not vim.g.neovide then
  return
end

vim.o.guifont = "Iosevkaterm Nerd Font,JetBrainsMono Nerd Font:h14"
-- vim.g.neovide_font = "JetBrainsMono Nerd Font:h12"
-- vim.o.guifont = "JetBrainsMono Nerd Font:h12"

vim.g.neovide_padding_top = 0
vim.g.neovide_padding_bottom = 0
vim.g.neovide_padding_right = 0
vim.g.neovide_padding_left = 0

vim.g.neovide_opacity = 1
vim.g.neovide_scroll_animation_length = 0.05
vim.g.neovide_cursor_animation_length = 0.05
vim.g.neovide_cursor_vfx_mode = ""
vim.g.neovide_refresh_rate = 144

vim.keymap.set({ "i", "t" }, "<C-S-v>", function()
  vim.api.nvim_paste(vim.fn.getreg("+"), true, -1)
end)
