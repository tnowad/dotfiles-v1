from libqtile.bar import CALCULATED
from libqtile.lazy import lazy

from core.bar.base import base, powerline, rectangle, symbol
from extras import Clock, GroupBox, TextBox, modify, widget
from utils.config import cfg
from utils.palette import palette

bar = {
    "background": palette.base,
    "border_color": palette.base,
    "border_width": 4,
    "margin": [0, 0, 0, 0],
    "opacity": 1,
    "size": 20,
}


def sep(fg, offset=0, padding=10):
    return TextBox(
        **base(None, fg),
        **symbol(11),
        offset=offset,
        padding=padding,
        text="󰇙",
    )


def logo(bg, fg): return TextBox(
    **base(bg, fg),
    **symbol(),
    **rectangle(),
    mouse_callbacks={"Button1": lazy.restart()},
    padding=20,
    text="",
)


def groups(bg): return GroupBox(
    **symbol(),
    background=bg,
    borderwidth=1,
    colors=[
        palette.teal,
        palette.pink,
        palette.yellow,
        palette.red,
        palette.blue,
        palette.green,
    ],
    highlight_color=palette.base,
    highlight_method="line",
    inactive=palette.surface2,
    invert=True,
    padding=6,
    rainbow=True,
)


def volume(bg, fg): return [
    modify(
        TextBox,
        **base(bg, fg),
        **symbol(),
        **rectangle("left"),
        offset=-17,
        padding=15,
        text="",
        x=-2,
    ),
    widget.Volume(
        **base(bg, fg),
        **powerline("arrow_right"),
        check_mute_command="pamixer --get-mute",
        check_mute_string="true",
        get_volume_command="pamixer --get-volume-human",
        mute_command="pamixer --toggle-mute",
        update_interval=0.1,
        volume_down_command="pamixer --decrease 5",
        volume_up_command="pamixer --increase 5",
    ),
]


def backlight(bg, fg): return [
    modify(
        TextBox,
        **base(bg, fg),
        **symbol(),
        **powerline("arrow_left"),
        offset=-17,
        padding=10,
        text="󰃟",
        x=-2,
    ),
    widget.Backlight(
        **base(bg, fg),
        **powerline("arrow_right"),
        step=5,
        backlight_name="amdgpu_bl1",
        change_command="brightnessctl set {}%",
    ),
]

def battery(bg, fg): return [
    modify(
        TextBox,
        **base(bg, fg),
        **symbol(14),
        offset=-1,
        padding=0,
        x=-2,
    ),
    widget.Battery(
        **base(bg, fg),
        **rectangle("right"),
        full_char='󱊣',
        charge_char='󱊥',
        discharge_char='󱊢',
        format='{char} {percent:2.0%}',
        hide_threshold=0.99,
    ),
]

def updates(bg, fg): return [
    TextBox(
        **base(bg, fg),
        **symbol(14),
        offset=-1,
        text="",
        x=-2,
    ),
    widget.CheckUpdates(
        **base(bg, fg),
        **rectangle("right"),
        colour_have_updates=fg,
        colour_no_updates=fg,
        custom_command=" " if cfg.is_xephyr else "checkupdates",
        display_format="{updates} updates  ",
        initial_text="No updates  ",
        no_update_string="No updates  ",
        padding=0,
        update_interval=3600,
    ),
]


def window_name(fg): return widget.WindowName(
    **base(None, fg),
    format="{name}",
    max_chars=60,
    width=CALCULATED,
)


def cpu(bg, fg): return [
    modify(
        TextBox,
        **base(bg, fg),
        **symbol(14),
        **rectangle("left"),
        offset=-13,
        padding=15,
        text="󰍛",
    ),
    widget.CPU(
        **base(bg, fg),
        **powerline("arrow_right"),
        format="{load_percent:.0f}%",
    ),
]


def ram(bg, fg): return [
    TextBox(
        **base(bg, fg),
        **symbol(14),
        offset=-1,
        padding=5,
        text="󰘚",
    ),
    widget.Memory(
        **base(bg, fg),
        **powerline("arrow_right"),
        format="{MemUsed: .0f}{mm} ",
        padding=-3,
    ),
]


def disk(bg, fg): return [
    TextBox(
        **base(bg, fg),
        **symbol(14),
        offset=-1,
        text="",
        x=-2,
    ),
    widget.DF(
        **base(bg, fg),
        **powerline("arrow_right"),
        format="{f} GB  ",
        padding=0,
        partition="/",
        visible_on_warn=False,
        warn_color=fg,
    ),
]


def clock(bg, fg): return [
    modify(
        TextBox,
        **base(bg, fg),
        **symbol(14),
        **rectangle("left"),
        offset=-14,
        padding=15,
        text="",
    ),
    modify(
        Clock,
        **base(bg, fg),
        **rectangle("right"),
        format="%A - %I:%M %p ",
        long_format="%B %-d, %Y ",
        padding=7,
    ),
]


def widgets(): return [
    widget.Spacer(length=1),
    logo(palette.blue, palette.base),
    sep(palette.surface2, offset=-14),
    groups(None),
    sep(palette.surface2, offset=8, padding=2),
    *volume(palette.blue, palette.base),
    *backlight(palette.pink, palette.base),
    *updates(palette.red, palette.base),
    widget.Spacer(),
    window_name(palette.text),
    widget.Spacer(),
    *cpu(palette.green, palette.base),
    *ram(palette.yellow, palette.base),
    *disk(palette.teal, palette.base),
    *battery(palette.peach, palette.base),
    sep(palette.surface2),
    *clock(palette.pink, palette.base),
    widget.Spacer(length=1),
]
