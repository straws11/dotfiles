### TODO:

- add .config/nvim as submodule maybe?
- add other stuff you forgot about
- setup this readme
- "nmcli device wifi connect "Capybara Enclosure v11.07" --ask" for wifi rn LOL
- fix the guy's waybar config in .config/waybar/config, loads of his stuff not mine, just a start

# Installation

## Dependencies

- Git (duh)
- GNU Stow:

```bash
pacman -S stow
```

## Use

Clone:
```bash
git clone git@github.com/straws11/dotfiles.git
cd dotfiles
```

Following to create the symlinks from the dotfiles dir to the system
```bash
stow .
```
