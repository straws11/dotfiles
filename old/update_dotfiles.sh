#!/bin/bash

BACKUP_DIR=~/dotfiles

echo -e "\033[0;31mThis action will override your current configs with the current $BACKUP_DIR contents. Make sure your current configs are backed up / definitely outdated!\033[0m"

read -p "Overwrite local configs with those from $BACKUP_DIR (y/n): " confirmation

if [ $confirmation != 'y' ]; then
	echo 'Skipping update process'
	exit 1
fi

# all dotfiles files
declare -a dot_files=(
[0]=.zshrc
[1]=.wezterm.lua
[2]=.tmux.conf
)

# copy all dotfiles into home
for i in ${dot_files[@]}
do
	cp $BACKUP_DIR/$i ~/
done

# make dirs if not existing
mkdir -p ~/.config/nvim/
mkdir -p ~/.oh-my-zsh/

# copy specific config dirs and files
cp -r $BACKUP_DIR/.config/nvim/* ~/.config/nvim/
cp -r $BACKUP_DIR/.oh-my-zsh/* ~/.oh-my-zsh/

echo -e "\033[0;32mDotfiles copied from $BACKUP_DIR\033[0m"
