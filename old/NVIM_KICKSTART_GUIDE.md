# Welcome to Straws11's kickstart.nvim starter guide [Messy WIP]

Disclaimer: Some parts of this guide assume you use [kickstart.nvim](https://github.com/nvim-lua/kickstart.nvim) or at least some of the plugins present in kickstart.

---

## Purpose of this Guide

- Some useful beginner (neo)vim keybinds
- Using LSP commands (kickstart defined)
- Summary of basic keybinds to get started

This guide does not aim to replace the kickstart.nvim guides. Kickstart is very well documented and is available in the `init.lua` file, you *should* make some time to read through it yourself!

See this as a super (and very incomplete) summary of what you can do with neovim + kickstart. The idea is to be able to start coding immediately, and being able to analyze the `init.lua` at your own pace, without being in the dark until then.

---

## Useful Keybinds

These can all be changed in your `init.lua` file.
For combinations, options for following keypresses show up after you hit a key. Try hitting `y` and wait.

### Combination Examples

- **ciw** - Change Inner Word
    - Try `d or y` instead of `c`
    - Try `a` instead of `i`
    - Try `" or { or ( or [` instead of `w`
- **ytx** - Yank To `x`
    - Test on this line: `exercise`
    - Try `d/c` instead of `y`
    - Try `T/f/F` instead of `t`


### Other Useful Keybinds

Keybinds I use in my daily workflow.
`<leader>` is set in `init.lua`, it will be the space character by default

- **C-o / C-i** - Jump back/forward to the previous/next place you were. This is great to use after something like `gd` or `gr` when you want to resume where you were
- **G** - Move to end of file
- **gg** - Move to top of file
- **\<leader>sf** - Search File names from directory nvim was launched in
- **\<leader>sg** - Search with Grep through files in directory nvim was launched in
- **C-y** - Used when you want to accept a highlighted suggestion
- **C-n / C-p** - Next and previous for various popup lists, faster than arrow keys
- **ZZ** - Save & Quit all open buffers and neovim. Alternative to `:wq`

### Language Server Protocol (LSP) Keybinds

In kickstart.nvim, the Mason plugin is used to install formatters, LSPs and other neat tools for different programming languages. Run `:Mason` from Normal Mode to open the Mason menu.

These bindings require an LSP to be installed for the current filetype / language. The LSP provides the ability to understand the language and provided the following:

- **K** - Shows Documentation for the variable / function etc. Type again to move cursor onto the popup.
- **gd** - Goto Definition for this variable
- **gr** - Goto References of this variable
