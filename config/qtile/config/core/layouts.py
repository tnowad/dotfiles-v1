from libqtile import layout
from utils.match import title, wm_class
from utils.palette import palette

config = {
    "border_focus": palette.pink,
    "border_normal": palette.base,
    "border_width": 0,
    "margin": 2,
    "single_border_width": 0,
    "single_margin": 2,
}

layouts = [
    layout.Columns(**config),
    # layout.MonadTall(
    #     **config,
    #     change_ratio=0.02,
    #     min_ratio=0.30,
    #     max_ratio=0.70,
    # ),
    # layout.Columns(border_focus_stack=[palette.base, palette.pink], border_width=1),
    layout.Max(**config),
    # Try more layouts by unleashing below layouts.
    # layout.Stack(num_stacks=2),
    # layout.Bsp(),
    # layout.Matrix(),
    # layout.MonadWide(),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]


floating_layout = layout.Floating(
    border_focus=palette.subtext1,
    border_normal=palette.base,
    border_width=0,
    fullscreen_border_width=0,
    float_rules=[
        *layout.Floating.default_float_rules,
        *wm_class(
            "confirmreset",
            "Display",
            "floating",
            "gnome-screenshot",
            "gpicview",
            "kvantummanager",
            "lxappearance",
            "makebranch",
            "maketag",
            "pavucontrol",
            "pinentry-gtk-2",
            "psterm",
            "qt5ct",
            "ssh-askpass",
            "steam",
            # "thunar",
            # "Thunar",
            "Xephyr",
            "xfce4-about",
        ),
        *title(
            "branchdialog",
            "minecraft-launcher",
            "pinentry",
        ),
    ],
)
