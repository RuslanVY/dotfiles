#!/bin/bash
# ~/.config/qtile/scripts/powermenu.sh
# Меню питания на rofi в стиле Gruvbox.
# Зависимости: rofi, systemctl (systemd), loginctl, qtile.
# Блокировка: используется первый найденный из i3lock / betterlockscreen / slock.
#
# chmod +x ~/.config/qtile/scripts/power-menu.sh

THEME="gruvbox-dark"

# ----- Пункты меню -----
lock="󰌾  Блокировка"
logout="󰍃  Выйти из сессии"
suspend="󰒲  Сон"
hibernate="󰤄  Гибернация"
reboot="󰜉  Перезагрузка"
shutdown="󰿅  Выключить"

yes="  Да"
no="  Нет"

# ----- Вызовы rofi -----
rofi_menu() {
  rofi -dmenu -i -p "Питание" -theme "$THEME" -no-custom \
    -theme-str 'window {width: 20em;} listview {lines: 6;}'
}

confirm() {
  # $1 - заголовок вопроса
  local answer
  answer=$(printf '%s\n%s\n' "$yes" "$no" | rofi -dmenu -i -p "$1" \
    -theme "$THEME" -no-custom \
    -theme-str 'window {width: 18em;} listview {lines: 2;}')
  [[ "$answer" == "$yes" ]]
}

# ----- Блокировка экрана -----
do_lock() {
  ~/.config/qtile/scripts/lock.sh
}

# ----- Выбор -----
chosen=$(printf '%s\n' \
  "$lock" "$logout" "$suspend" "$hibernate" "$reboot" "$shutdown" | rofi_menu)

# Esc или пустой выбор - просто выйти
[[ -z "$chosen" ]] && exit 0

case "$chosen" in
"$lock")
  do_lock
  ;;
"$logout")
  confirm "Выйти из сессии?" && qtile cmd-obj -o cmd -f shutdown
  ;;
"$suspend")
  systemctl suspend
  ;;
"$hibernate")
  confirm "Гибернация?" && systemctl hibernate
  ;;
"$reboot")
  confirm "Перезагрузить?" && systemctl reboot
  ;;
"$shutdown")
  confirm "Выключить компьютер?" && systemctl poweroff
  ;;
esac
