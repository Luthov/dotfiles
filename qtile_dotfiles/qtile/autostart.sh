#!/bin/sh

xrandr --output DP-2 --mode 1920x1080 --rate 144
nm-applet &
polybar &
picom &
