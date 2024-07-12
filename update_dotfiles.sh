#!/bin/bash

BACKUP_DIR=~/dotfiles

git pull origin main

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

echo -e '\033[0;32mDotfiles restored/updated from repo\033[0m'
