#!/bin/bash
# ~/.config/qtile/scripts/autostart.sh

# Обязательно нужно делать файл исполняемым командой:
# chmod +x ~/.config/qtile/scripts/autostart.sh

# & - ставится для запуска программы в фоне
# pgrep - проверяет программу на повторный запуск или запуск вообще

# ----- Обои -----
# feh --bg-fill
pgrep waypaper || waypaper --restore &

# ----- Композитор x11 -----
pgrep picom || picom &

# ----- Уведомления -----
pgrep dunst || dunst &

# ----- Интернет NetworkManagerAppled -----
# создаёт икону в трее
pgrep nm-applet || nm-applet &

# ----- Блютуз Blueman -----
# создаёт икону в трее
pgrep blueman-applet || blueman-applet &

# ----- Буфер обмена -----
# ----- Clipboard -----
pgrep copyq || copyq &

# ----- Скриншоты -----
# ----- Flameshot -----
pgrep flameshot || flameshot &

# ----- Polkit-агент -----
pgrep -f polkit-gnome-authentication-agent-1 || /usr/lib/polkit-gnome/polkit-gnome-authentication-agent-1 &

# ----- Блокировка экрана -----
# Блокировка после 10 минут простоя (600 с), предупреждение за 30 с
xset s 600 30
xset s on
pgrep -x xss-lock >/dev/null || xss-lock --transfer-sleep-lock \
  --notifier="notify-send -u low 'Скоро блокировка экрана'" \
  -- "$HOME/.config/qtile/scripts/lock.sh" &
