#!/bin/bash

sudo pacman -S git

mkdir ~/Github/
cd Github/
sudo pacman -S --needed git base-devel && git clone https://aur.archlinux.org/yay.git && cd yay && makepkg -si

yay -S alacritty lightdm qtile zsh pavucontrol picom flameshot neovim playerctl catppuccin-gtk-theme-macchiato papirus-folders-catppuccin-git network-manager-applet


chsh -s $(which zsh)
