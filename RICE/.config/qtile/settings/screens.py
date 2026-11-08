from libqtile import bar, widget
from libqtile.lazy import lazy
from libqtile.config import Screen
from settings.theme import colors, font, fontsize
from settings.keys import rmenu, rpower_menu

# ─────────────────────────────────────────────
#  Настройки виджетов
# ─────────────────────────────────────────────
widget_defaults = dict(
    font=font,
    fontsize=fontsize,
    padding=5,
    background=colors["bg_hard"],
    foreground=colors["fg"],
)
extension_defaults = widget_defaults.copy()

# ─────────────────────────────────────────────
#  Экраны и панель
# ─────────────────────────────────────────────
screens = [
    Screen(
        top=bar.Bar(
            [
                # ── Лого / кнопка меню ──────   
                widget.TextBox(
                    text=" ",
                    fontsize=25,
                    foreground=colors["yellow"],
                    background=colors["bg_hard"],
                    padding=5,
                    mouse_callbacks={"Button1": lazy.spawn(rmenu)},
                ),
                widget.Sep(
                    linewidth=1,
                    padding=2,
                    foreground=colors["bg2"],
                    background=colors["bg_hard"],
                ),
                # ── Группы ──────────────────
                widget.GroupBox(
                    margin_y=3,
                    margin_x=4,
                    padding_y=5,
                    padding_x=6,
                    borderwidth=2,
                    active=colors["fg"],
                    inactive=colors["bg4"],
                    rounded=True,
                    highlight_method="line",
                    highlight_color=colors["bg_hard"],
                    this_current_screen_border=colors["yellow"],
                    this_screen_border=colors["yellow"],
                    other_current_screen_border=colors["aqua"],
                    other_screen_border=colors["aqua"],
                    foreground=colors["fg"],
                    background=colors["bg_hard"],
                    urgent_alert_method="line",
                    urgent_border=colors["red_bright"],
                    disable_drag=True,
                    # Скрывать пустые группы.
                    # hide_unused=True,
                ),
                widget.Sep(
                    linewidth=1,
                    padding=12,
                    foreground=colors["bg2"],
                    background=colors["bg_hard"],
                ),
                # ── Текущий лейаут ──────────
                widget.CurrentLayout(
                    mode="both",
                    icon_first=True,
                    # custom_icon_paths=["~/.config/qtile/icons/layout"],
                    foreground=colors["fg4"],
                    background=colors["bg_hard"],
                    fontsize=14,
                    padding=5,
                    scale=0.50,
                ),
                widget.Sep(
                    linewidth=1,
                    padding=12,
                    foreground=colors["bg2"],
                    background=colors["bg_hard"],
                ),
                # ── Имя окна ────────────────
                widget.WindowName(
                    foreground=colors["fg2"],
                    background=colors["bg_hard"],
                    fontsize=14,
                    max_chars=60,
                    format="{name}",
                    mouse_callbacks={"Button1": lazy.window.toggle_minimize()},
                ),
                # ── Правая часть ─────────────
                # widget.Spacer(background=colors["bg_hard"]),
                widget.Sep(
                    linewidth=1,
                    padding=12,
                    foreground=colors["bg2"],
                    background=colors["bg_hard"],
                ),
                widget.WidgetBox(
                    widgets=[
                        # NET
                        widget.Net(
                            format="󰖩  ↓{down:.0f}{down_suffix} ↑{up:.0f}{up_suffix}",
                            interface=None,
                            use_bits=True,
                            update_interval=1.0,
                            foreground=colors["red_bright"],
                            background=colors["bg_hard"],
                            fontsize=14,
                            padding=5,
                        ),
                        widget.Sep(
                            linewidth=1,
                            padding=12,
                            foreground=colors["bg2"],
                            background=colors["bg_hard"],
                        ),
                        widget.CPU(
                            background=colors["bg_hard"],
                            foreground=colors["aqua_bright"],
                            format=" {load_percent:.0f}%",
                            update_interval=2,
                            fontsize=14,
                        ),
                        widget.TextBox(
                            text="",
                            foreground=colors["aqua_bright"],
                            background=colors["bg_hard"],
                            fontsize=16,
                        ),
                        widget.ThermalSensor(
                            threshold=75,
                            background=colors["bg_hard"],
                            foreground=colors["aqua_bright"],
                            fontsize=14,
                        ),
                        widget.Sep(
                            linewidth=1,
                            padding=12,
                            foreground=colors["bg2"],
                            background=colors["bg_hard"],
                        ),
                        # RAM
                        widget.Memory(
                            background=colors["bg_hard"],
                            foreground=colors["blue_bright"],
                            fontsize=14,
                            format=" {MemUsed:.0f}{mm}",
                            measure_mem="M",
                            update_interval=2,
                        ),
                        widget.Sep(
                            linewidth=1,
                            padding=12,
                            foreground=colors["bg2"],
                            background=colors["bg_hard"],
                        ),
                        widget.DF(
                            partition="/home",
                            format="󰋊 {uf:.0f}{m}",
                            visible_on_warn=False,
                            warn_space=20,
                            warn_color=colors["red_bright"],
                            update_interval=60,
                            foreground=colors["red_bright"],
                            background=colors["bg_hard"],
                            fontsize=14,
                            padding=5,
                        ),
                        widget.Sep(
                            linewidth=1,
                            padding=12,
                            foreground=colors["bg2"],
                            background=colors["bg_hard"],
                        ),
                    ],
                    rotate=True,
                    close_button_location="right",
                    text_closed="󰺔",
                    text_open="󰺔",
                    fontsize=20,
                    foreground=colors["orange_bright"],
                ),
                widget.Sep(
                    linewidth=1,
                    padding=12,
                    foreground=colors["bg2"],
                    background=colors["bg_hard"],
                ),
                widget.WidgetBox(
                    widgets=[
                        # Громкость
                        # yay -S python-pulsectl-asyncio
                        widget.PulseVolume(
                            fmt="  {}",
                            limit_max_volume=True,
                            mouse_callbacks={"Button1": lazy.spawn("pavucontrol")},
                            # ---
                            background=colors["bg_hard"],
                            foreground=colors["blue_bright"],
                            fontsize=14,
                            padding=5,
                        ),
                        widget.Sep(
                            linewidth=1,
                            padding=12,
                            foreground=colors["bg2"],
                            background=colors["bg_hard"],
                        ),
                        widget.Backlight(
                            # ls /sys/class/backlighta/
                            backlight_name="intel_backlight", # amdgpu_bl1
                            foreground=colors["orange_bright"],
                            format="󰖨 {percent:2.0%}",
                            fontsize=14,
                            change_command="brightnessctl set {0}%",
                            update_interval=1,
                        ),
                        widget.Sep(
                            linewidth=1,
                            padding=12,
                            foreground=colors["bg2"],
                            background=colors["bg_hard"],
                        ),
                        widget.Battery(
                            battery="BAT1",
                            format="{char} {percent:2.0%}", # [{hour:d}:{min:02d}]
                            update_interval=60,
                            show_short_text=False,
                            hide_threshold=None,
                            # ---
                            charge_char="󰂄",
                            discharge_char="󱧥",
                            full_char="󰁹",
                            empty_char="󰂎",
                            unknown_char="󰂑",
                            # ---
                            fontsize=14,
                            padding=5,
                            low_percentage=0.20,
                            foreground=colors["green_bright"],
                            background=colors["bg_hard"],
                            low_foreground=colors["red"],
                            charging_foreground=colors["purple"],
                        ),
                        widget.Sep(
                            linewidth=1,
                            padding=12,
                            foreground=colors["bg2"],
                            background=colors["bg_hard"],
                        ),
                    ],
                    close_button_location="right",
                    text_closed="󰀻",
                    text_open="󰀻",
                    fontsize=23,
                    foreground=colors["aqua"],
                ),
                widget.Sep(
                    linewidth=1,
                    padding=12,
                    foreground=colors["bg2"],
                    background=colors["bg_hard"],
                ),
                widget.WidgetBox(
                    widgets=[
                        # Системный трей 
                        widget.Systray(
                            background=colors["bg_hard"],
                            padding=6,
                        ),
                    ],
                    close_button_location="right",
                    text_closed="󰙅",
                    text_open="󱏒",
                    fontsize=20,
                    foreground=colors["blue_bright"],
                ),
                widget.Sep(
                    linewidth=1,
                    padding=12,
                    foreground=colors["bg2"],
                    background=colors["bg_hard"],
                ),
                # Раскладка клавиатуры
                # требуется установка пакета "xorg-setxkbmap"
                widget.KeyboardLayout(
                    configured_keyboards=["us", "ru"],
                    display_map={"us": "EN", "ru": "RU"},
                    foreground=colors["gray"],
                    background=colors["bg_hard"],
                    fontsize=14,
                    padding=5,
                ),
                widget.Sep(
                    linewidth=1,
                    padding=12,
                    foreground=colors["bg2"],
                    background=colors["bg_hard"],
                ),
                # Дата и время
                widget.Clock(
                    background=colors["bg_hard"],
                    foreground=colors["yellow_bright"],
                    format="󱑂 %H:%M",  # %a %d %b
                    fontsize=14,
                    # Открыть календарь
                    mouse_callbacks={"Button1": lazy.spawn("gsimplecal")},
                ),
                widget.Sep(
                    linewidth=1,
                    padding=12,
                    foreground=colors["bg2"],
                    background=colors["bg_hard"],
                ),
                # widget.Pomodoro(),
                # Кнопка выхода
                widget.TextBox(
                    text="󰿅",
                    foreground=colors["red_bright"],
                    background=colors["bg_hard"],
                    fontsize=25,
                    padding=8,
                    # mouse_callbacks={"Button1": lazy.shutdown()},
                    mouse_callbacks={"Button1": lazy.spawn(rpower_menu)},
                ),
            ],
            size=34,
            background=colors["bg_hard"],
            margin=[6, 6, 0, 6],  # top, right, bottom, left
            opacity=0.9,
        ),
    ),
]
