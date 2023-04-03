#!/usr/bin/env zsh
polybar-msg cmd quit
polybar main 2>&1 & disown
