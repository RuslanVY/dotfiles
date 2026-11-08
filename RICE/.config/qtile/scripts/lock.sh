#!/bin/sh
# Экран блокировки: своя картинка + Gruvbox dark

IMG="$HOME/.config/qtile/pictures/Закат над крепостью_ ритуал на утёсе.png"

exec i3lock --nofork \
  --image="$IMG" --fill \
  --clock --indicator \
  --ind-pos="x+w/4:y+h/2+10" \
  --radius=30 --ring-width=5 \
  --time-pos="x+w/4:y+h/2-80" --date-pos="tx:ty+30" \
  --time-str="%H:%M" --date-str="%A, %d %B" \
  --time-size=96 --date-size=24 \
  --time-color=ebdbb2ff --date-color=a89984ff \
  --inside-color=00000000 --ring-color=ebdbb2ff \
  --line-color=00000000 --separator-color=00000000 \
  --keyhl-color=1d2021ff --bshl-color=fe8019ff \
  --ringver-color=8ec07cff --verif-color=8ec07cff \
  --ringwrong-color=fb4934ff --wrong-color=fb4934ff \
  --insidever-color=00000000 --insidewrong-color=00000000 \
  --verif-text="" --wrong-text="" --noinput-text=""
