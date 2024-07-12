#!/bin/bash

BACKUP_DIR=~/dotfiles
DEFAULT_COMMIT_MSG='Updated dotfiles'

git pull origin main

echo -e '\033[0;32mType your commit message, leave blank for default\033[0m'

read commit_message

if [ "$commit_message" == '' ]; then
	commit_message=$DEFAULT_COMMIT_MSG
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

git add .
git commit -m "$commit_message"
git push origin main

echo -e '\033[0;32mDotfiles backed up to repo\033[0m'
