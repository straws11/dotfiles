import os
import sys
from enum import Enum

# INFO MESSAGE CONSTS
TMUX_INFO = "Tmux is a terminal multiplexer. It allows you to open multiple panes & windows (like tabs) in a single terminal application. Useful if you want to keep (neo)vim open and be able to run code or execute other terminal commands."
WEZTERM_INFO = "Wezterm is a terminal application. It is an alternative to the \"Terminal\" application that you are used to. You can safely ignore this one and keep using Terminal if you want to."
ZSH_INFO = "ZSH (Z-Shell) is an alternative to Bash. Highly recommended to use OhMyZsh with this."
OHMYZSH_INFO = "OhMyZsh is a framework for ZSH (ZSH has to be installed). It allows you to pick some nice preset themes and has plugins that are straightforward to enable."
NVIM_INFO = "NeoVim is a refactored Vim, which allows for more customizability. It makes installing plugins and themes easy. Highly recommended."

class ConfigType(Enum):
    FILE = 1
    DIR = 2

class ConfigItem():
    def __init__(self, name: str, path: str, info_msg: str, file_type: ConfigType) -> None:
        self._name = name
        self._file_type = file_type
        self._path = path
        self._info = info_msg

    def get_type(self) -> ConfigType:
        return self._file_type

    def get_path(self) -> str:
        return self._path

    def get_name(self) -> str:
        return self._name

    def get_info_msg(self) -> str:
        return self._info

def main():
    print('Welcome to Straws11\'s dotfiles script!')
    items = create_items()
    print('\nPlease type y/n to indicate whether you would like the specified configuration file to be included in the install\n')
    items_filtered: list[ConfigItem] = filter_items(items)
    install_configs(items_filtered)
    print(f"\nInstallation done! Installed {len(items_filtered)} configs.\nMake sure to read the documentation on these configs")


def execute_cmd(command: str) -> None:
    '''Execute command in shell, or print if debug param passed'''
    if len(sys.argv) > 1:
        if sys.argv[1] == "--debug":
            print(command)
        else:
            print("Did you mean \"--debug\"?")
    else:
        os.system(command)


def install_configs(config_items: list[ConfigItem]) -> None:
    '''Copies all user-selected config files from this repo into their respective directories'''
    for item in config_items:
        path = item.get_path()
        # create parent dirs, if necessary
        # TODO: move this logic into the ConfigItem, some sort of path processing methods
        if path.count('/') > 1: # only ~/ should be in the path
            execute_cmd("mkdir -p " + "~/testy" + path[:path.rindex('/')][1:])
        execute_cmd(f"cp {"-r" if item.get_type() == ConfigType.DIR else ""} ./{path[2:]} ~/testy/{path[2:]}")
        print(f"Installed {item.get_name()}'s config")


def create_items() -> list[ConfigItem]:
    '''Init all config items that I support'''
    return [
        ConfigItem('NeoVim','~/.config/nvim', OHMYZSH_INFO, ConfigType.DIR),
        ConfigItem('Z-Shell', '~/.zshrc', ZSH_INFO, ConfigType.FILE),
        ConfigItem('OhMyZsh', '~/.oh-my-zsh', OHMYZSH_INFO, ConfigType.DIR),
        ConfigItem('tmux', '~/.tmux.conf', TMUX_INFO, ConfigType.FILE),
        ConfigItem('WezTerm', '~/.wezterm.lua', WEZTERM_INFO, ConfigType.FILE),
    ]


def filter_items(items: list[ConfigItem]) -> list[ConfigItem]:
    '''Queries users on the available items and returns the list of config's they want'''
    filtered: list[ConfigItem] = []
    for item in items:
        while True:
            print(f"Would you like to install {item.get_name()}'s configuration? (y/n): ", end='')
            confirmation = input().lower()
            # force user to type y or n
            if len(confirmation) == 0:
                continue

            match confirmation:
                case 'y':
                    filtered.append(item)
                    break
                case 'n':
                    break
                case _:
                    print("Please type 'y' or 'n'\n")
    return filtered


if __name__ == "__main__":
    main()
