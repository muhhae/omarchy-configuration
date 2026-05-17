return {
  "stevearc/aerial.nvim",
  opts = {
    backends = { "treesitter", "lsp", "markdown", "man" },
    filter_kind = {
      "Class",
      "Constructor",
      "Enum",
      "Function",
      "Struct",
      "Variable", -- Add this
      "Constant", -- Add this
    },
    show_guides = true,
  },
}
