from libqtile import bar, layout, widget
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
from utils.config import cfg
from utils.keybinding import show_keys 
from extras import float_to_front

if cfg.is_xephyr:
    mod, alt = "mod1", "control"
    restart = lazy.restart(),
else:
    mod, alt = "mod4", "mod1"
    restart = lazy.reload_config(),

if not cfg.term:
    cfg.term = guess_terminal(),

keys = [
    # Movement and window focus
    Key([mod], "h", lazy.layout.left(), desc="Move focus to the window on the left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to the window on the right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus to the window below"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus to the window above"),
    Key([mod], "space", lazy.layout.next(), desc="Cycle window focus to the next window"),

    # Move windows between columns
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move the window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(), desc="Move the window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move the window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move the window up"),

    # Increase/decrease window size
    Key([mod, "control"], "h", lazy.layout.grow_left(), desc="Expand window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(), desc="Expand window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Expand window downward"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Expand window upward"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),

    # Window management
    Key([mod, "shift"], "Return", lazy.layout.toggle_split(), desc="Toggle between split and unsplit stack sides"),
    Key([], "F11", lazy.window.toggle_fullscreen(), desc="Toggle fullscreen mode"),

    # Launch terminal
    Key([mod], "Return", lazy.spawn(cfg.term), desc="Open the terminal"),
    Key([mod, "shift"], "Return", lazy.spawn(cfg.term2), desc="Open another terminal"),

    # Layout and window operations
    Key([mod], "Tab", lazy.next_layout(), desc="Switch between different layouts"),
    Key([mod], "w", lazy.window.kill(), desc="Close the focused window"),

    # Qtile specific actions
    Key([mod, "control"], "b", lazy.hide_show_bar(), desc="Show/Hide the status bar"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the Qtile configuration"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),

    # Spawn applications
    Key([mod], "r", lazy.spawn("rofi -show drun"), desc="Open the application launcher"),
    Key([mod, "shift"], "r", lazy.spawn("rofi -show window"), desc="Open the window switcher"),

    # Media control and brightness
    Key([], "XF86AudioLowerVolume", lazy.spawn("pamixer --decrease 5"), desc="Decrease audio volume"),
    Key([], "XF86AudioRaiseVolume", lazy.spawn("pamixer --increase 5"), desc="Increase audio volume"),
    Key([], "XF86AudioMute", lazy.spawn("pamixer --toggle-mute"), desc="Toggle audio mute/unmute"),
    Key([], "XF86MonBrightnessUp", lazy.spawn("brightnessctl set +10%"), desc="Increase screen brightness"),
    Key([], "XF86MonBrightnessDown", lazy.spawn("brightnessctl set 10%-"), desc="Decrease screen brightness"),

    # Screenshot tool
    Key([], "Print", lazy.spawn("gnome-screenshot -i"), desc="Take a screenshot"),
    Key(["shift"], "Print", lazy.spawn("gnome-screenshot -i"), desc="Take a screenshot of the active window"),
    Key(["control"], "Print", lazy.spawn("gnome-screenshot -i -a"), desc="Take a screenshot of a selected area"),
    Key([mod], "Print", lazy.spawn("gnome-screenshot -i -c"), desc="Take a screenshot and copy it to the clipboard"),
    Key([mod, "shift"], "Print", lazy.spawn("gnome-screenshot -i -c"), desc="Take a screenshot of the active window and copy it to the clipboard"),
    Key([mod, "control"], "Print", lazy.spawn("gnome-screenshot -i -c -a"), desc="Take a screenshot of a selected area and copy it to the clipboard"),
]

keys.extend([Key([mod], "F1", lazy.spawn("sh -c 'echo \"" + show_keys(keys) + "\" | rofi -dmenu -i -mesg \"Keyboard shortcuts\"'"), desc="Print keyboard bindings"),])
