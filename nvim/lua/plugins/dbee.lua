return {
  "kndndrj/nvim-dbee",
  dependencies = {
    "MunifTanjim/nui.nvim",
  },
  opts = {
    call_log = {
      height = 0,
    },
  },
  keys = {
    {
      "<leader>D",
      function()
        require("dbee").toggle()
      end,
      desc = "Toggle dbee UI",
    },
  },
  build = function()
    -- Install tries to automatically detect the install method.
    -- if it fails, try calling it with one of these parameters:
    --    "curl", "wget", "bitsadmin", "go"
    require("dbee").install()
  end,
  config = function()
    require("dbee").setup(--[[optional config]])
  end,
}
