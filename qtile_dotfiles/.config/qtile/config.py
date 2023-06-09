import os
import subprocess

from libqtile import bar, layout, widget, hook
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal

mod = "mod4"
terminal = guess_terminal()

bg = "#222436"
fg = "#c8d3f5"
cyan = "#86e1fc"
blue = "#65bcff"
magenta = "#c099ff"
orange = "#ff966c"
yellow = "#ffc777"
green = "#c3e88d"
teal = "#4fd6be"
red = "#ff757f"

# ███████ ████████  █████  ██████  ████████ ██    ██ ██████
# ██         ██    ██   ██ ██   ██    ██    ██    ██ ██   ██
# ███████    ██    ███████ ██████     ██    ██    ██ ██████
#      ██    ██    ██   ██ ██   ██    ██    ██    ██ ██
# ███████    ██    ██   ██ ██   ██    ██     ██████  ██

@hook.subscribe.startup_once
def autostart():
    # .expanduser is to make sure that it starts at $HOME when "~" is at the start
    startup_script = os.path.expanduser("~/.config/qtile/autostart.sh")
    subprocess.Popen([startup_script])

# ██   ██ ███████ ██    ██ ██████  ██ ███    ██ ██████  ██ ███    ██  ██████  ███████ 
# ██  ██  ██       ██  ██  ██   ██ ██ ████   ██ ██   ██ ██ ████   ██ ██       ██      
# █████   █████     ████   ██████  ██ ██ ██  ██ ██   ██ ██ ██ ██  ██ ██   ███ ███████ 
# ██  ██  ██         ██    ██   ██ ██ ██  ██ ██ ██   ██ ██ ██  ██ ██ ██    ██      ██ 
# ██   ██ ███████    ██    ██████  ██ ██   ████ ██████  ██ ██   ████  ██████  ███████

keys = [
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),

    Key([mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),

    Key([mod, "control"], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),

    # Application keybindings
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    Key([mod], "b", lazy.spawn("firefox"), desc="Launch firefox"),
    Key([mod], "e", lazy.spawn("thunar"), desc="Launch thunar"),
    Key([mod, "shift"], "t", lazy.spawn("telegram-desktop"), desc="Launch telegram"),
    Key([mod, "shift"], "e", lazy.spawn("element-desktop"), desc="Launch element"),
    Key([mod, "shift"], "d", lazy.spawn("discord"), desc="Launch discord"),
    Key([mod, "shift"], "s", lazy.spawn("flameshot gui"), desc="Launch screenshot"),
    Key([mod], "r", lazy.spawn("sh /home/luthov15/.config/rofi/bin/launcher"), desc="Launch screenshot"),

    # Media keybindings
    Key([], "XF86AudioRaiseVolume", lazy.spawn("pactl set-sink-volume @DEFAULT_SINK@ +5%"), desc="Increase Volume"),
    Key([], "XF86AudioLowerVolume", lazy.spawn("pactl set-sink-volume @DEFAULT_SINK@ -5%"), desc="Lower Volume"),
     Key([], "XF86AudioMute", lazy.spawn("pactl set-sink-mute @DEFAULT_SINK@ toggle"), desc="Mute"),
     Key([], "XF86Launch1", lazy.spawn("playerctl play-pause"), desc="Pause-play"),

    # Brightness keybindings
    Key([], "XF86MonBrightnessUp", lazy.spawn("brightnessctl set +10%"), desc="Increase Brightness"),
    Key([], "XF86MonBrightnessDown", lazy.spawn("brightnessctl set 10%-"), desc="Decrease Brightness"),
    Key([], "XF86KbdBrightnessUp", lazy.spawn("brightnessctl -d asus::kbd_backlight set 1+"), desc="Increase kbd Brightness"),
    Key([], "XF86KbdBrightnessDown", lazy.spawn("brightnessctl -d asus::kbd_backlight set 1-"), desc="Decrease kbd Brightness"),
    
    # Power keybindings
    Key([mod, "control"], "s", lazy.spawn("poweroff"), desc="Poweroff"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),

    # Toggle between different layouts as defined below
    Key([mod], "q", lazy.window.kill(), desc="Kill focused window"),
    Key([mod], "f", lazy.window.toggle_fullscreen(), desc="Toggle fullscreen"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
]

# ██     ██  ██████  ██████  ██   ██ ███████ ██████   █████   ██████ ███████ ███████ 
# ██     ██ ██    ██ ██   ██ ██  ██  ██      ██   ██ ██   ██ ██      ██      ██      
# ██  █  ██ ██    ██ ██████  █████   ███████ ██████  ███████ ██      █████   ███████ 
# ██ ███ ██ ██    ██ ██   ██ ██  ██       ██ ██      ██   ██ ██      ██           ██ 
#  ███ ███   ██████  ██   ██ ██   ██ ███████ ██      ██   ██  ██████ ███████ ███████ 

groups = [Group(i) for i in "12345"]

for i in groups:
    keys.extend(
        [
            # mod1 + letter of group = switch to group
            Key(
                [mod],
                i.name,
                lazy.group[i.name].toscreen(),
                desc="Switch to group {}".format(i.name),
            ),
            # mod1 + shift + letter of group = switch to & move focused window to group
            Key(
                [mod, "shift"],
                i.name,
                lazy.window.togroup(i.name, switch_group=True),
                desc="Switch to & move focused window to group {}".format(i.name),
            ),
            # Or, use below if you prefer not to switch to that group.
            # # mod1 + shift + letter of group = move focused window to group
            # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
            #     desc="move focused window to group {}".format(i.name)),
        ]
    )
    
# ██       █████  ██    ██  ██████  ██    ██ ████████ ███████ 
# ██      ██   ██  ██  ██  ██    ██ ██    ██    ██    ██      
# ██      ███████   ████   ██    ██ ██    ██    ██    ███████ 
# ██      ██   ██    ██    ██    ██ ██    ██    ██         ██ 
# ███████ ██   ██    ██     ██████   ██████     ██    ███████ 

layouts = [
        layout.Columns(border_focus=[cyan], border_width=2, margin=3),
    layout.Max(),
    # Try more layouts by unleashing below layouts.
    # layout.Stack(num_stacks=2),
    # layout.Bsp(),
    # layout.Matrix(),
    # layout.MonadTall(),
    # layout.MonadWide(),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

# ███    ███  ██████  ██    ██ ███████ ███████
# ████  ████ ██    ██ ██    ██ ██      ██
# ██ ████ ██ ██    ██ ██    ██ ███████ █████
# ██  ██  ██ ██    ██ ██    ██      ██ ██
# ██      ██  ██████   ██████  ███████ ███████

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

# ███████  ██████ ██████  ███████ ███████ ███    ██ ███████ 
# ██      ██      ██   ██ ██      ██      ████   ██ ██      
# ███████ ██      ██████  █████   █████   ██ ██  ██ ███████ 
#      ██ ██      ██   ██ ██      ██      ██  ██ ██      ██ 
# ███████  ██████ ██   ██ ███████ ███████ ██   ████ ███████

widget_defaults = dict(
    font="CaskaydiaCove Nerd Font MononCaskaydiaCove Nerd Font Mono SemiBold",
    fontsize=12,
    padding=3,
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        #top=bar.Bar(
        #    [ 
        #        # widget.BatteryIcon(),
        #        widget.PulseVolume(emoji = True),
        #        widget.Systray(),
        #        widget.Spacer(),
        #        widget.GroupBox(),
        #        widget.Spacer(),
        #        widget.Clock(format="%Y/%m/%d %a %I:%M %p"),
        #    ],
        #    24,
        #    margin = [3, 3, 0, 3]
        #    
        #),

        wallpaper = "~/.wallpapers/boat_abondoned.jpg",
        wallpaper_mode = "fill", # Other option is stretch
    ),
]

# ███    ███ ██ ███████  ██████ 
# ████  ████ ██ ██      ██      
# ██ ████ ██ ██ ███████ ██      
# ██  ██  ██ ██      ██ ██      
# ██      ██ ██ ███████  ██████ ██

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ]
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
