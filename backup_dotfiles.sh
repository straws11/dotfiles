#!/bin/bash

BACKUP_DIR=~/dotfiles

echo -e "\033[0;31mThis action will override the current "$BACKUP_DIR" contents. Ensure changes are committed.\033[0m"

# git status
echo -e '\033[0;46mRunning git status:\033[0m'
(cd ~/dotfiles && git status)
echo

read -p "Copy files into $BACKUP_DIR (y/n): " confirmation

if [ $confirmation != 'y' ]; then
	echo 'Skipping backup process'
	exit 1
fi


# all dotfiles files
declare -a dot_files=(
[0]=.zshrc
[1]=.wezterm.lua
[3]=.tmux.conf
)

# copy all dotfiles to the backup_dir
for i in ${dot_files[@]}
do
	cp ~/$i $BACKUP_DIR
done

# make dirs if not existing
mkdir -p $BACKUP_DIR/.config/nvim/
mkdir -p $BACKUP_DIR/.oh-my-zsh/custom/

# copy specific config dirs and files
cp ~/.config/nvim/{init.lua,lazy-lock.json,.stylua.toml} $BACKUP_DIR/.config/nvim
cp -R ~/.config/nvim/{doc,lua} $BACKUP_DIR/.config/nvim
cp -R ~/.oh-my-zsh/custom $BACKUP_DIR/.oh-my-zsh

echo -e "\033[0;32mFiles Backed up into $BACKUP_DIR\033[0m"
