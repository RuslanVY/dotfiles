from libqtile import layout
from libqtile.config import Match
from settings.theme import colors

# ─────────────────────────────────────────────
#  Лейауты
# ─────────────────────────────────────────────
layout_theme = {
    "border_width": 2,
    "margin": 8,
    "border_focus": colors["yellow"],
    "border_normal": colors["bg2"],
}

layouts = [
    layout.Columns(
        **layout_theme,
        border_focus_stack=colors["orange"],
    ),
    layout.MonadTall(
        **layout_theme,
        ratio=0.55,
    ),
    layout.MonadWide(
        **layout_theme,
    ),
    layout.Max(
        border_width=0,
        margin=0,
    ),
]

# ─────────────────────────────────────────────
#  Плавающие окна (правила)
# ─────────────────────────────────────────────
floating_layout = layout.Floating(
    border_focus=colors["orange"],
    border_normal=colors["bg2"],
    border_width=2,

    float_rules=[
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),
        Match(wm_class="makebranch"),
        Match(wm_class="maketag"),
        Match(wm_class="ssh-askpass"),
        Match(wm_class="pinentry"),
        Match(wm_class="Arandr"),
        Match(wm_class="pavucontrol"),
        Match(wm_class="Nm-connection-editor"),
        Match(wm_class="Gsimplecal"),
        Match(wm_class="copyq"),
        Match(wm_class="Blueman-manager"),
        Match(wm_class="flameshot"),
        Match(wm_class="Waypaper"),
        Match(title="branchdialog"),
        Match(title="pinentry"),
    ],
)
