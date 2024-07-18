import os
import sys
import subprocess
from enum import Enum


# COLORS
class Color(Enum):
    RED = "\033[31m"
    BOLD = "\033[1m"
    CLEAR = "\033[0m"


class ConfigType(Enum):
    FILE = 1
    DIR = 2


# INFO MESSAGE CONSTS
TMUX_INFO = "Tmux\n\ta terminal multiplexer. It allows you to open multiple panes & windows (like tabs) in a single terminal application. Useful if you want to keep (neo)vim open and be able to run code or execute other terminal commands."
WEZTERM_INFO = 'Wezterm\n\ta terminal application. It is an alternative to the "Terminal" application that you are used to. You can safely ignore this one and keep using Terminal if you want to.'
OHMYZSH_INFO = "OhMyZsh\n\ta framework for ZSH (ZSH (an alternative to Bash) has to be installed). It allows you to pick some nice preset themes and has plugins that are straightforward to enable."
NVIM_INFO = "NeoVim\n\ta refactored Vim, which allows for more customizability. It makes installing plugins and themes easy. Highly recommended."

# RAW GITHUB CONTENT LINKS


CHOICE_MENU: str = (
    "Please select one of the below:\n\t'l' - see information about all available configs\n\t'i' - start selecting configs for install\n\t'q' - quit the application\n"
    + Color.BOLD.value
    + "[straws-config]#"
    + Color.CLEAR.value
)


class ConfigItem:
    def __init__(
        self,
        name: str,
        path: str,
        info_msg: str,
        file_type: ConfigType,
        extra: str = "",
    ) -> None:
        self._name = name
        self._file_type = file_type
        self._path = path
        self._info = info_msg
        self._extra_info = extra

    def get_type(self) -> ConfigType:
        return self._file_type

    def get_path(self) -> str:
        return self._path

    def get_name(self) -> str:
        return self._name

    def get_info_msg(self) -> str:
        return self._info

    def get_extra(self) -> str:
        return self._extra_info


def main():
    print("Welcome to Straws11's dotfiles script!")
    items = create_items()

    while True:
        user_choice = input(CHOICE_MENU)
        match user_choice:
            case "q":
                print("Quitting.. Bye!")
                sys.exit(0)
            case "l":
                list_config_infos()
            case "i":
                install_process(items)


def list_config_infos() -> None:
    """Lists all configs' info"""
    print(f"{NVIM_INFO}\n\n{OHMYZSH_INFO}\n\n{TMUX_INFO}\n\n{WEZTERM_INFO}\n\n")


def install_process(items: list[ConfigItem]) -> None:
    """Start the process to let user select configs to install, and then installing them"""
    print(
        f"{Color.RED.value}Any config you choose to install will OVERWRITE your existing config. This is irreversable!! Ctrl-C to abort{Color.CLEAR.value}"
    )
    print(
        "\nPlease type y/n to indicate whether you would like the specified configuration file to be included in the install\n"
    )
    items_filtered: list[ConfigItem] = filter_items(items)
    install_configs(items_filtered)
    print(
        f"\nInstallation done! Installed {len(items_filtered)} configs.\nMake sure to read the documentation on these configs"
    )


def execute_cmd(command: str) -> None:
    """Execute command in shell, or print if debug param passed"""
    if len(sys.argv) > 1:
        if sys.argv[1] == "--debug":
            print(command)
        else:
            print('Did you mean "--debug"?')
    else:
        os.system(command)


def install_configs(config_items: list[ConfigItem]) -> None:
    """Copies all user-selected config files from this repo into their respective directories"""
    for item in config_items:

        # ohmyzsh has different script
        if item.get_name() == "OhMyZsh":
            process = subprocess.Popen("which curl", stdout=subprocess.PIPE, shell=True)
            if process.returncode:  # if failed
                print(
                    "Please install the 'curl' package to be able to install OhMyZsh."
                )
                config_items.remove(item)  # fix install count in output message
                continue
            execute_cmd(
                'sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"'
            )
            continue

        path = item.get_path()
        # create parent dirs, if necessary
        # TODO: move this logic into the ConfigItem, some sort of path processing methods
        if path.count("/") > 1:  # only ~/ should be in the path
            execute_cmd("mkdir -p " + path[: path.rindex("/")])
        execute_cmd(
            f"cp {"-r" if item.get_type() == ConfigType.DIR else ""} ./{path[2:]} {path}"
        )
        print(f"Installed {item.get_name()}'s config")


def create_items() -> list[ConfigItem]:
    """Init all config items that I support"""
    return [
        ConfigItem("NeoVim", "~/.config/nvim", NVIM_INFO, ConfigType.DIR),
        ConfigItem(
            "OhMyZsh",
            "~/.oh-my-zsh",
            OHMYZSH_INFO,
            ConfigType.DIR,
            extra="This will install the default OhMyZsh framework for you",
        ),
        ConfigItem("tmux", "~/.tmux.conf", TMUX_INFO, ConfigType.FILE),
        ConfigItem("WezTerm", "~/.wezterm.lua", WEZTERM_INFO, ConfigType.FILE),
    ]


def filter_items(items: list[ConfigItem]) -> list[ConfigItem]:
    """Queries users on the available items and returns the list of config's they want"""
    filtered: list[ConfigItem] = []
    for item in items:
        while True:
            print(
                f"Would you like to install {item.get_name()}'s configuration? {item.get_extra()}(y/n): ",
                end="",
            )
            confirmation = input().lower()
            # force user to type y or n
            if len(confirmation) == 0:
                continue

            match confirmation:
                case "y":
                    filtered.append(item)
                    break
                case "n":
                    break
                case _:
                    print("Please type 'y' or 'n'\n")
    return filtered


if __name__ == "__main__":
    main()
