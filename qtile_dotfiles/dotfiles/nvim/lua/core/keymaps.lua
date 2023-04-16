vim.g.mapleader = ' '
vim.g.maplocalleader = ' '

vim.opt.number = true
vim.opt.showcmd = true
vim.opt.cursorline = true
vim.api.nvim_set_keymap('n', '<leader>t', ':ToggleTerm<CR>', {noremap = true})
