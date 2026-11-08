import os
from libqtile.config import Key
from libqtile.lazy import lazy

# ─────────────────────────────────────────────
#  Основные настройки
# ─────────────────────────────────────────────
mod = "mod4"
terminal = "kitty"
browser = "firefox"
file_manager = "thunar"
waypapers = "waypaper"
rmenu = "rofi -show drun -theme gruvbox-dark"
rlayout_menu = "rofi -show window -theme gruvbox-dark"
rpower_menu = os.path.expanduser("~/.config/qtile/scripts/powermenu.sh")
shots = os.path.expanduser("~/Images/Pictures")


# ─────────────────────────────────────────────
#  Горячие клавиши
# ─────────────────────────────────────────────
keys = [
    # ── Навигация по окнам ──────────────────
    Key([mod], "h", lazy.layout.left(), desc="Фокус влево"),
    Key([mod], "l", lazy.layout.right(), desc="Фокус вправо"),
    Key([mod], "j", lazy.layout.down(), desc="Фокус вниз"),
    Key([mod], "k", lazy.layout.up(), desc="Фокус вверх"),
    Key([mod, "shift"], "space", lazy.layout.next(), desc="Следующее окно"),
    
    # ── Перемещение окон ────────────────────
    Key([mod, "shift"], "h", lazy.layout.shuffle_left().when(layout="columns"), lazy.layout.swap_left().when(layout=["monadtall", "monadwide"]), desc="Переместить влево"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right().when(layout="columns"), lazy.layout.swap_right().when(layout=["monadtall", "monadwide"]), desc="Переместить вправо"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Переместить вниз"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Переместить вверх"),
    
    # ── Изменение размера окон ──────────────
    Key([mod, "control"], "h", lazy.layout.grow_left().when(layout="columns"), lazy.layout.shrink().when(layout=["monadtall", "monadwide"]), desc="Уменьшить мастер / сдвинуть границу влево"),
    Key([mod, "control"], "l", lazy.layout.grow_right().when(layout="columns"), lazy.layout.grow().when(layout=["monadtall", "monadwide"]), desc="Увеличить мастер / сдвинуть границу вправо"),
    Key([mod, "control"], "j", lazy.layout.grow_down().when(layout="columns"), lazy.layout.shrink_main().when(layout=["monadtall", "monadwide"]), desc="Увеличить вниз"),
    Key([mod, "control"], "k", lazy.layout.grow_up().when(layout="columns"), lazy.layout.grow_main().when(layout=["monadtall", "monadwide"]), desc="Увеличить вверх"),
    Key([mod], "n", lazy.layout.normalize(), desc="Сбросить размеры"),
    
    # ── Лейауты ─────────────────────────────
    Key([mod], "Tab", lazy.next_layout(), desc="Следующий лейаут"),
    Key([mod, "shift"], "Tab", lazy.prev_layout(), desc="Предыдущий лейаут"),
    Key([mod], "f", lazy.window.toggle_fullscreen(), desc="Полный экран"),
    Key([mod, "shift"], "f", lazy.window.toggle_floating(), desc="Плавающее окно"),
    
    # ── Управление окнами ───────────────────
    Key([mod], "q", lazy.window.kill(), desc="Закрыть окно"),
    Key(["mod1"], "Tab", lazy.spawn(rlayout_menu), desc="Меню переключения окон"),
    
    # ── Приложения ──────────────────────────
    Key([mod], "Return", lazy.spawn(terminal), desc="Терминал"),
    Key([mod], "b", lazy.spawn(browser), desc="Браузер"),
    Key([mod], "e", lazy.spawn(file_manager), desc="Файловый менеджер"),
    Key([mod], "w", lazy.spawn(waypapers), desc="Менеджер обоев"),
    Key([mod], "r", lazy.spawn(rmenu), desc="Меню запуска"),
    
    # ── Скриншоты ───────────────────────────
    Key([], "Print", lazy.spawn("flameshot gui"), desc="Скриншот области"),
    Key(["shift"], "Print", lazy.spawn("flameshot full -p " + shots), desc="Весь экран"),

    # ── Звук ───────────────────────────
    Key([], "XF86AudioRaiseVolume", lazy.spawn("wpctl set-volume -l 1.0 @DEFAULT_AUDIO_SINK@ 5%+")),
    Key([], "XF86AudioLowerVolume",lazy.spawn("wpctl set-volume @DEFAULT_AUDIO_SINK@ 5%-")),
    Key([], "XF86AudioMute",lazy.spawn("wpctl set-mute @DEFAULT_AUDIO_SINK@ toggle")),

    # ── Яркость ─────────────────────────────
    Key([], "XF86MonBrightnessUp", lazy.spawn("brightnessctl set +10%")),
    Key([], "XF86MonBrightnessDown", lazy.spawn("brightnessctl set 10%-")),

    # ── Qtile ───────────────────────────────
    Key([mod, "control"], "r", lazy.reload_config(), desc="Перезагрузить конфиг"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Выйти из Qtile"),

    # ── En/Ru ───────────────────────────────
    Key([mod], "space", lazy.widget["keyboardlayout"].next_keyboard(), desc="Переключить раскладку"),
    
    Key([mod], "z", lazy.spawn(rpower_menu), desc="Меню питания"),
    Key([mod], "x", lazy.spawn("loginctl lock-session"), desc="Заблокировать экран"),
]
