# dotfiles
My dotfiles, managed by a simple (and somewhat manual script).
Includes Python installation script.

---

## USAGE

### Starter Install Script

If you want to use some of my starter configs, I recommend using the `install.py` installation script. It guides you through the process, and can provide information about the applications the configs are for.

#### Using the Install Script

To use the installation script, run `python install.py`. You will enter an interactive prompt, from which you can install, get information, or quit.

If you choose `i` to install configs, you will be prompted for each of the config files I have available. You need only select the ones you want.

#### Valuable Links

I only have the configuration files available, you will need to install the applications themselves. You can find them here:

- [NeoVim](https://github.com/neovim/neovim/blob/master/INSTALL.md)
- [Zsh](https://github.com/ohmyzsh/ohmyzsh/wiki/Installing-ZSH)
- [Tmux](https://github.com/tmux/tmux)
- [Wezterm](https://wezfurlong.org/wezterm/install/linux.html)

<sub>Note: OhMyZsh IS a config, you don't need to install anything outside of my config.</sub>

### General Usage for Dotfiles

If you want to use my shell scripts to maintain your own dotfiles, you may use the below scripts in your own repo

**Instructions**: 

Copy files from their declared local locations into the repo root:

    ./backup_dotfiles.sh

Copy files from the repo root into their local locations:
    
    ./update_dotfiles.sh

There are some warnings and confirmations to help prevent overwriting any configs.
    
---

## Kickstart.nvim QuickStart Guide

Check out my (wip) [Kickstart Quickstart Guide](NVIM_KICKSTART_GUIDE.md) to help you get started with some basics of kickstart, using either mine or the official [kickstart.nvim](https://github.com/nvim-lua/kickstart.nvim). I cannot guarantee that this is up to date.

