# Copyright (c) 2010 Aldo Cortesi
# Copyright (c) 2010, 2014 dequis
# Copyright (c) 2012 Randall Ma
# Copyright (c) 2012-2014 Tycho Andersen
# Copyright (c) 2012 Craig Barnes
# Copyright (c) 2013 horsik
# Copyright (c) 2013 Tao Sauvage
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from libqtile import bar, layout, widget, extension
from libqtile.config import Click, Drag, Group, Key, Match, Screen, Match
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal

import os

mod = "mod1"
terminal = "alacritty"
CaskaydiaFont = 'CaskaydiaCove Nerd Font Mono'

colors = [
    "#282c34",
    "#1c1f24",
    "#e06c75",
    "#98c379",
    "#e5c07b",
    "#61afef",
    "#c678dd",
    "#56b6c2",
    "#abb2bf"]

keys = [
    # A list of available commands that can be bound to keys can be found
    # at https://docs.qtile.org/en/latest/manual/config/lazy.html
    # Switch between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(),
        desc="Move window focus to other window"),
    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(),
        desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(),
        desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),
    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "h", lazy.layout.grow_left(),
        desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(),
        desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key(
        [mod, "shift"],
        "Return",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",
    ),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    # Key([mod], "r", lazy.spawncmd(), desc="Spawn a command using a prompt widget"),
    Key([mod], "r", lazy.run_extension(extension.DmenuRun(
        dmenu_ignorecase=True,
        dmenu_prompt="UwU",
        dmenu_font=CaskaydiaFont,
        background=colors[0],
        foreground=colors[2],
        selected_background=colors[6],
        selected_foreground=colors[1],
    ))),
]

#groups = [Group(i) for i in "123456789"]

__groups = {
    1: Group("???"),
    2: Group("???"),
    3: Group("???"),
    4: Group("???"),
    5: Group("???"),
    8: Group("???"),
    9: Group("???"),
    0: Group("???"),
}

groups = [__groups[i] for i in __groups]


def get_group_key(name):
    return [k for k, g in __groups.items() if g.name == name][0]


def incBrightness():
    os.system("brightnessctl s +10%")


def decBrightness():
    os.system("brightnessctl s 10%-")


for i in groups:
    keys.extend(
        [
            # mod1 + letter of group = switch to group
            Key(
                [mod],
                str(get_group_key(i.name)),
                lazy.group[i.name].toscreen(),
                desc="Switch to group {}".format(i.name),
            ),
            # mod1 + shift + letter of group = switch to & move focused window to group
            Key(
                [mod, "shift"],
                str(get_group_key(i.name)),
                lazy.window.togroup(i.name, switch_group=True),
                desc="Switch to & move focused window to group {}".format(
                    i.name),
            ),
            # Or, use below if you prefer not to switch to that group.
            # # mod1 + shift + letter of group = move focused window to group
            # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
            #     desc="move focused window to group {}".format(i.name)),
        ]
    )

layouts = [
    # layout.Columns(
    #    border_focus_stack=["#d75f5f", "#8f3d3d"],
    #    border_width=4,
    #    margin=4
    #    ),
    # Try more layouts by unleashing below layouts.
    # layout.Stack(num_stacks=2),
    # layout.Bsp(
    #    margin=4,
    #    ),
    # layout.Matrix(),
    layout.MonadTall(
        margin=5,
        single_border_width=0,
        single_margin=0,
        border_focus="#51afef",
        border_normal="#777777",
        border_width=2,
    ),
    layout.Max(),
    # layout.MonadWide(),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

widget_defaults = dict(
    font="CaskaydiaCove Mono Nerd Font",
    fontsize=17,
    padding=1,
    background=colors[0]
)
extension_defaults = widget_defaults.copy()

fsize = 15



screens = [
    Screen(
        top=bar.Bar(
            [
                #widget.CurrentLayout(font=CaskaydiaFont, ontsize=fsize),
                #widget.Spacer(length = 10),
                # widget.Sep(),
                #widget.Spacer(length = 5),
                widget.GroupBox(
                    font=CaskaydiaFont,
                    fontsize=27,
                    margin_y=3,
                    margin_x=0,
                    padding_y=8,
                    padding_x=5,
                    this_current_screen_border=colors[6],
                    borderwidth=1,
                    inactive="777777",
                    rounded=False,
                    highlight_method='block',
                    urgent_alert_method='block',
                    disable_drag=True,
                ),
                widget.Spacer(length=10),
                widget.Sep(
                    linewidth=0,
                    padding=6,
                    foreground="#333333",
                    background="#333333"
                ),
                widget.Spacer(length=10),
                widget.WindowName(font=CaskaydiaFont,
                                  fontsize=fsize, padding=5),
                widget.Chord(
                    chords_colors={
                        "launch": ("#ff0000", "#ffffff"),
                    },
                    name_transform=lambda name: name.upper(),
                ),

                widget.TextBox(
                    text='???',
                    font="Ubuntu Mono",
                    background=colors[0],
                    foreground=colors[2],
                    padding=-0.1,
                    fontsize=37
                ),
                widget.ThermalSensor(
                    font=CaskaydiaFont,
                    foreground=colors[1],
                    background=colors[2],
                    threshold=90,
                    fmt='Temp: {}',
                    padding=5
                ),
                widget.TextBox(
                    text='???',
                    font="Ubuntu Mono",
                    background=colors[2],
                    foreground=colors[3],
                    padding=-0.1,
                    fontsize=37
                ),
                widget.Systray(
                    foreground=colors[1],
                    padding=5,
                    margin=10,
                    background=colors[3]
                ),
                widget.Sep(  # Separator to fucking flameshot
                    linewidth=5,
                    foreground=colors[3],
                    background=colors[3]
                ),
                widget.TextBox(
                    text='???',
                    font="Ubuntu Mono",
                    background=colors[3],
                    foreground=colors[4],
                    padding=-0.1,
                    fontsize=37
                ),
                widget.Battery(
                    foreground=colors[1],
                    font=CaskaydiaFont,
                    background=colors[4],
                    padding=5,
                    update_interval=15,
                    format='??? {percent:2.0%} {char} {hour:d}:{min:02d}h'
                ),
                widget.TextBox(
                    text='???',
                    font="Ubuntu Mono",
                    background=colors[4],
                    foreground=colors[5],
                    padding=-0.1,
                    fontsize=37
                ),
                widget.TextBox(
                    text="???", font=CaskaydiaFont,
                    fontsize=27,
                    padding=5,
                    background=colors[5],
                    foreground=colors[1],
                ),
                widget.Volume(
                    font=CaskaydiaFont,
                    foreground=colors[1],
                    background=colors[5],
                    fmt='{} ',
                    padding=5
                ),
                widget.TextBox(
                    text='???',
                    font="Ubuntu Mono",
                    background=colors[5],
                    foreground=colors[6],
                    padding=-0.1,
                    fontsize=37
                ),
                # widget.KeyboardLayout(
                #       foreground = colors[1],
                #       background = colors[6],
                #       configured_keyboards=['latam','us'],
                #       padding = 5
                #       ),
                widget.TextBox(
                    text="???", font=CaskaydiaFont,
                    fontsize=27,
                    padding=5,
                    background=colors[6],
                    foreground=colors[1],
                ),
                widget.Backlight(
                    font=CaskaydiaFont,
                    backlight_name='amdgpu_bl0',
                    mouse_callbacks={'Button1': incBrightness,
                                     'Button3': decBrightness},
                    fmt="{} ",
                    foreground=colors[1],
                    background=colors[6]
                ),
                widget.TextBox(
                    text='???',
                    font="Ubuntu Mono",
                    background=colors[6],
                    foreground=colors[7],
                    padding=-0.1,
                    fontsize=37
                ),
                widget.TextBox(
                    text="???", font=CaskaydiaFont,
                    fontsize=27,
                    padding=7,
                    background=colors[7],
                    foreground=colors[1],
                ),
                widget.Clock(
                    font=CaskaydiaFont,
                    foreground=colors[1],
                    background=colors[7],
                    format="%d/%m/%y - %H:%M "
                ),

            ],
            25,
            # border_width=[0, 0, 0, 0],  # Draw top and bottom borders
            # border_color=["ff00ff", "000000", "ff00ff", "000000"]  # Borders are magenta
        ),
    ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

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
auto_fullscreen = False
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

autostart = [
    "feh --bg-fill /home/koch/Pictures/Wallpapers/onedark.png",
    "picom --no-vsync &"
]

for x in autostart:
    os.system(x)
