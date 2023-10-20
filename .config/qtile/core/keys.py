from libqtile import bar, layout, widget
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
# import widgets
from utils.config import cfg
from extras import float_to_front

# if cfg.is_xephyr:
#     mod, alt = "mod1", "control"
#     restart = lazy.restart()
# else:
#     mod, alt = "mod4", "mod1"
#     restart = lazy.reload_config()
#
# if not cfg.term:
#     cfg.term = guess_terminal()
#

mod = "mod4"
terminal = guess_terminal()

keys = [
    # switch between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(),
        desc="Move window focus to other window"),

    # move windows between columns
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(),
        desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(),
        desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),

    # increase/decrease window size
    Key([mod, "control"], "h", lazy.layout.grow_left(),
        desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(),
        desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),

    # window management
    Key(
        [mod, "shift"],
        "Return",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",
    ),
    Key([], "F11", lazy.window.toggle_fullscreen(), desc="Toggle fullscreen"),

    # floating window management
    # Key([mod], "space", lazy.window.toggle_floating()),
    # Key([mod], "s", lazy.function(float_to_front)),
    # Key([mod], "c", lazy.window.center()),

    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),

#     # qtile stuff
    Key([mod, "control"], "b", lazy.hide_show_bar(), desc="Hide show bar"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),

    Key([mod], "r", lazy.spawn("rofi -show run"), desc="Spawn a command using a prompt widget"),
    Key([mod, "shift"], "r", lazy.spawncmd()),
    Key([], "XF86AudioLowerVolume", lazy.spawn("pamixer --decrease 5")),
    Key([], "XF86AudioRaiseVolume", lazy.spawn("pamixer --increase 5")),
    Key([], "XF86AudioMute", lazy.spawn("pamixer --toggle-mute")),
    Key([], "XF86MonBrightnessUp", lazy.spawn("brightnessctl set +10%")),
    Key([], "XF86MonBrightnessDown", lazy.spawn("brightnessctl set 10%-")),

    # screenshot tool
    Key([], "Print", lazy.spawn("gnome-screenshot -i"), desc="Take a screenshot"),
    Key(["shift"], "Print", lazy.spawn("gnome-screenshot -i"), desc="Take a screenshot of a window"),
    Key(["control"], "Print", lazy.spawn("gnome-screenshot -i -a"), desc="Take a screenshot of an area"),
    Key([mod], "Print", lazy.spawn("gnome-screenshot -i -c"), desc="Take a screenshot to clipboard"),
    Key([mod, "shift"], "Print", lazy.spawn("gnome-screenshot -i -c"), desc="Take a screenshot of a window to clipboard"),
    Key([mod, "control"], "Print", lazy.spawn("gnome-screenshot -i -c -a"), desc="Take a screenshot of an area to clipboard"),
]

widget_defaults = dict(
    font="sans",
    fontsize=12,
    padding=3,
)
extension_defaults = widget_defaults.copy()
#
# screens = [
#     Screen(
#         bottom=bar.Bar(
#             [
#                 widget.CurrentLayout(),
#                 widget.GroupBox(),
#                 widget.Prompt(),
#                 widget.WindowName(),
#                 widget.Chord(
#                     chords_colors={
#                         "launch": ("#ff0000", "#ffffff"),
#                     },
#                     name_transform=lambda name: name.upper(),
#                 ),
#                 widget.TextBox("default config", name="default"),
#                 widget.TextBox("Press &lt;M-r&gt; to spawn",
#                                foreground="#d75f5f"),
#                 # NB Systray is incompatible with Wayland, consider using StatusNotifier instead
#                 # widget.StatusNotifier(),
#                 widget.Systray(),
#                 widget.Clock(format="%Y-%m-%d %a %I:%M %p"),
#                 widget.QuickExit(),
#                 # widgets.Battery(update_interval=60),
#             ],
#             24,
#             # border_width=[2, 0, 2, 0],  # Draw top and bottom borders
#             # border_color=["ff00ff", "000000", "ff00ff", "000000"]  # Borders are magenta
#         ),
#     ),
# ]
#
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


def show_keys():
    key_help = ""
    for k in keys:
        mods = ""

        for m in k.modifiers:
            if m == "mod4":
                mods += "Super + "
            else:
                mods += m.capitalize() + " + "

        if len(k.key) > 1:
            mods += k.key.capitalize()
        else:
            mods += k.key

        key_help += "{:<30} {}".format(mods, k.desc + "\n")

    return key_help


keys.extend([Key([mod], "F1", lazy.spawn("sh -c 'echo \"" + show_keys() +
            "\" | rofi -dmenu -i -mesg \"Keyboard shortcuts\"'"), desc="Print keyboard bindings"),])
# keys = [Key(*key) for key in [  # type: ignore
#     # switch between windows
#     ([mod], "h", lazy.layout.left()),
#     ([mod], "n", lazy.layout.down()),
#     ([mod], "e", lazy.layout.up()),
#     ([mod], "i", lazy.layout.right()),
#
#     # move windows between columns
#     ([mod, "shift"], "h", lazy.layout.shuffle_left()),
#     ([mod, "shift"], "n", lazy.layout.shuffle_down()),
#     ([mod, "shift"], "e", lazy.layout.shuffle_up()),
#     ([mod, "shift"], "i", lazy.layout.shuffle_right()),
#
#     # increase/decrease window size
#     ([mod], "u", lazy.layout.shrink()),
#     ([mod], "y", lazy.layout.grow()),
#
#     # window management
#     ([mod, "shift"], "space", lazy.layout.flip()),
#     ([mod], "m", lazy.layout.maximize()),
#     ([mod], "a", lazy.window.kill()),
#     ([], "F11", lazy.window.toggle_fullscreen()),
#
#     # toggle between layouts
#     ([mod], "Tab", lazy.next_layout()),
#
#     # qtile stuff
#     ([mod, "control"], "b", lazy.hide_show_bar()),
#     ([mod, "control"], "s", lazy.shutdown()),
#     ([mod, "control"], "r", restart),
#
#     # terminal
#     ([mod], "Return", lazy.spawn(cfg.term)),
#     ([mod, "shift"], "Return", lazy.spawn(cfg.term2)),
#
#     # app launcher
#     ([mod, "shift"], "r", lazy.spawn("rofi -show window")),
#     ([mod], "r", lazy.spawn("rofi -show drun")),
#
#     # web browser
#     ([mod], "b", lazy.spawn(cfg.browser)),
#
# ]]  # fmt: skip
