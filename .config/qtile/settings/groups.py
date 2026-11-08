from libqtile.config import Group, Key, Match
from libqtile.lazy import lazy
from settings.keys import keys, mod

# ─────────────────────────────────────────────
#  Группы (рабочие пространства)
# ─────────────────────────────────────────────
groups = [
    Group("1", label=""),
    Group("2", label=""),
    Group("3", label="", matches=[Match(wm_class="firefox")], layout="columns"),
    Group("4", label="󰟐"),
    Group("5", label="󰌳"),
    Group("6", label=""),
    Group("7", label=""),
]

for g in groups:
    keys.extend(
        [
            Key(
                [mod],
                g.name,
                lazy.group[g.name].toscreen(),
                desc=f"Переключиться на группу {g.name}",
            ),
            Key(
                [mod, "shift"],
                g.name,
                lazy.window.togroup(g.name, switch_group=True),
                desc=f"Переместить окно в группу {g.name}",
            ),
        ]
    )

